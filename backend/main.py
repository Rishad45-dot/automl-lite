import base64
import io
import uuid
import warnings
from typing import Any, IO, Tuple, cast, Optional

from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.figure import Figure
import numpy as np
import pandas as pd
from pandas.api.types import (
    is_bool_dtype,
    is_string_dtype,
    is_numeric_dtype,
    is_datetime64_any_dtype,
    is_categorical_dtype,
)
from sklearn.ensemble import (
    RandomForestClassifier,
    RandomForestRegressor,
)
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    f1_score,
    mean_squared_error,
    precision_score,
    recall_score,
    r2_score,
)
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC, SVR
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor

plt.switch_backend("Agg")

app = FastAPI()

dataset_cache: dict[str, pd.DataFrame] = {}

# Allow frontend running on another origin to make requests to this backend.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------------------------------------------------------
# Strict mapping to prevent model/task mismatches
# ------------------------------------------------------------
TASK_MODEL_MAP = {
    "classification": [
        "LogisticRegression",
        "RandomForestClassifier",
        "DecisionTreeClassifier",
        "SVM"
    ],
    "regression": [
        "LinearRegression",
        "RandomForestRegressor",
        "DecisionTreeRegressor",
        "SVR"
    ]
}

@app.get("/")
def read_root():
    return {"message": "Backend is running"}

@app.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
    has_header: Optional[bool] = None
) -> dict[str, Any]:
    filename = file.filename or ""
    if not filename.lower().endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only .csv files are allowed")

    try:
        contents = await file.read()
        header_df: pd.DataFrame = pd.read_csv(io.BytesIO(contents), header=0)
        raw_df: pd.DataFrame = pd.read_csv(io.BytesIO(contents), header=None)
    except Exception as exc:
        raise HTTPException(status_code=400, detail=f"Failed to parse CSV: {exc}")

    def row_is_numeric(row: pd.Series) -> bool:
        return bool(pd.to_numeric(row, errors="coerce").notna().all())

    def row_is_string(row: pd.Series) -> bool:
        def _is_string(value: Any) -> bool:
            return isinstance(value, str)
        return bool(row.apply(_is_string).all())

    first_row = raw_df.iloc[0]
    second_row = raw_df.iloc[1] if len(raw_df) > 1 else None

    # Improved header detection: checks if AT LEAST one cell in the second row is numeric.
    auto_has_header = False
    if second_row is not None:
        first_row_is_string = row_is_string(first_row)
        second_row_has_numeric = bool(pd.to_numeric(second_row, errors="coerce").notna().any())
        
        auto_has_header = first_row_is_string and second_row_has_numeric
        
        if row_is_numeric(first_row):
            auto_has_header = False

    final_has_header = has_header if has_header is not None else auto_has_header

    data_df = header_df if final_has_header else raw_df

    target_series: pd.Series = data_df.iloc[:, -1]
    cleaned_target = target_series.dropna()
    if len(cleaned_target) == 0:
        raise HTTPException(status_code=400, detail="Target column contains no valid data.")

    if is_bool_dtype(cleaned_target.dtype):
        detected_task = "classification"
    elif is_string_dtype(cleaned_target.dtype):
        detected_task = "classification"
    elif isinstance(cleaned_target.dtype, pd.CategoricalDtype):
        detected_task = "classification"
    elif is_numeric_dtype(cleaned_target.dtype):
        unique_count = int(cleaned_target.nunique(dropna=True))
        detected_task = "classification" if unique_count <= 10 else "regression"
    else:
        detected_task = "classification"

    suggested_target = str(data_df.columns[-1])
    session_id = str(uuid.uuid4())
    dataset_cache[session_id] = data_df

    preview = data_df.head(5).to_dict(orient="records")

    return {
        "session_id": session_id,
        "columns": list(data_df.columns.astype(str)),
        "preview": preview,
        "has_header_guess": final_has_header,
        "detected_task": detected_task,
        "target_column": suggested_target,
    }


class TrainRequest(BaseModel):
    session_id: str
    target_column: str
    task_type: str
    model_name: str


# ------------------------------------------------------------
# Robust feature preprocessing
# Handles datetimes, strings, categories, and mixed types.
# ------------------------------------------------------------
def prepare_features(df: pd.DataFrame, target_column: str) -> tuple[pd.DataFrame, pd.Series]:
    if target_column not in df.columns:
        raise ValueError(f"Target column '{target_column}' not found in DataFrame")

    target = df[target_column]
    valid_idx = target.dropna().index
    if valid_idx.empty:
        raise ValueError("Target column contains no valid data.")

    # Separate features and target
    X = df.loc[valid_idx].drop(columns=[target_column])
    y = target.loc[valid_idx]

    # Check if there are any feature columns left
    if X.shape[1] == 0:
        raise ValueError(
            "No feature columns available after removing the target. "
            "Please upload a dataset with at least one predictor column."
        )

    # Make a copy to avoid modifying the original cached DataFrame
    X = X.copy()

    # 1. Identify and convert non-numeric columns
    non_numeric_cols = []
    for col in X.columns:
        # Skip columns that are already numeric
        if is_numeric_dtype(X[col]):
            continue

        # If it's datetime, convert to string first (so get_dummies will work)
        if is_datetime64_any_dtype(X[col]):
            X[col] = X[col].astype(str)

        # If it's any other non-numeric type (object, string, category), mark it
        if not is_numeric_dtype(X[col]):
            non_numeric_cols.append(col)

    # 2. One-hot encode all non-numeric columns
    if non_numeric_cols:
        X = pd.get_dummies(X, columns=non_numeric_cols, drop_first=False)

    # 3. Final safety check: Ensure every column is now numeric
    for col in X.columns:
        if not is_numeric_dtype(X[col]):
            # Raise a clear error pointing to the problematic column
            sample_value = X[col].iloc[0] if len(X) > 0 else "N/A"
            raise ValueError(
                f"Column '{col}' (sample value: '{sample_value}') could not be converted to numeric features. "
                "Please ensure your data contains only numerical values or clean text labels."
            )

    return X, y


def render_image(fig: Figure) -> str:
    buffer = io.BytesIO()
    fig.savefig(cast(IO[bytes], buffer), format="png")
    plt.close(fig)
    buffer.seek(0)
    return base64.b64encode(buffer.read()).decode("utf-8")


# ------------------------------------------------------------
# render_histogram kept but no longer called (optional)
# ------------------------------------------------------------
def render_histogram(series: pd.Series, title: str) -> str:
    buffer = io.BytesIO()
    fig, ax = cast(Tuple[Figure, Axes], plt.subplots())
    ax.hist(series.to_numpy(dtype=float), bins=20, color="#4c72b0", edgecolor="black")
    ax.set_title(title)
    ax.set_xlabel(series.name if series.name is not None else "")
    ax.set_ylabel("Frequency")
    fig.tight_layout()
    fig.savefig(cast(IO[bytes], buffer), format="png")
    plt.close(fig)
    buffer.seek(0)
    return base64.b64encode(buffer.read()).decode("utf-8")


# ------------------------------------------------------------
# UPDATED: Stats endpoint – shows only the target column, no histogram
# ------------------------------------------------------------
@app.get("/stats")
def stats(session_id: str, target_column: Optional[str] = None) -> dict[str, Any]:
    if session_id not in dataset_cache:
        raise HTTPException(status_code=404, detail="Session ID not found")

    df = dataset_cache[session_id]
    
    # If target_column is not provided, default to the last column
    if target_column is None:
        target_column = df.columns[-1]
    
    # Validate target column exists
    if target_column not in df.columns:
        raise HTTPException(
            status_code=400,
            detail=f"Target column '{target_column}' not found in DataFrame. Available: {list(df.columns)}"
        )
    
    # Check if the target column is numeric
    if not is_numeric_dtype(df[target_column].dtype):
        raise HTTPException(
            status_code=400,
            detail=f"Target column '{target_column}' is not numeric. Statistics are only available for numeric targets."
        )

    series = df[target_column].dropna()
    if series.empty:
        raise HTTPException(status_code=400, detail="Target column contains no valid data.")

    desc = series.describe(percentiles=[0.25, 0.5, 0.75])

    stats_response = {
        "column": target_column,
        "mean": float(desc["mean"]),
        "std": float(desc["std"]),
        "min": float(desc["min"]),
        "25%": float(desc["25%"]),
        "50%": float(desc["50%"]),
        "75%": float(desc["75%"]),
        "max": float(desc["max"]),
        "count": int(desc["count"]),
    }

    return {"stats": stats_response}


# ------------------------------------------------------------
# HELPER: Format target name for display
# ------------------------------------------------------------
def format_label(name: str) -> str:
    """Replace underscores with spaces and capitalize words."""
    return name.replace('_', ' ').title()


# ------------------------------------------------------------
# UPDATED: render_confusion_matrix with target name in title
# ------------------------------------------------------------
def render_confusion_matrix(y_true: pd.Series, y_pred: np.ndarray, target_name: str) -> str:
    cm = confusion_matrix(y_true, y_pred)
    # Convert to strings to avoid dtype mismatches
    true_labels = y_true.astype(str).to_numpy()
    pred_labels = y_pred.astype(str)
    labels = np.unique(np.concatenate([true_labels, pred_labels]))
    
    fig, ax = cast(Tuple[Figure, Axes], plt.subplots())
    cax = ax.imshow(cm, interpolation="nearest", cmap="Blues")
    fig.colorbar(cax, ax=ax)
    
    # Use formatted target name in title
    formatted_name = format_label(target_name)
    ax.set_title(f"Confusion Matrix for {formatted_name}")
    ax.set_xlabel("Predicted")
    ax.set_ylabel("Actual")
    ax.set_xticks(np.arange(len(labels)))
    ax.set_yticks(np.arange(len(labels)))
    ax.set_xticklabels(labels, rotation=45, ha="right")
    ax.set_yticklabels(labels)

    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(j, i, int(cm[i, j]), ha="center", va="center", color="black")

    fig.tight_layout()
    return render_image(fig)


# ------------------------------------------------------------
# UPDATED: render_regression_scatter with target name in labels
# ------------------------------------------------------------
def render_regression_scatter(y_true: pd.Series, y_pred: np.ndarray, target_name: str) -> str:
    fig, ax = cast(Tuple[Figure, Axes], plt.subplots())
    y_true_np = y_true.to_numpy(dtype=float)
    y_pred_np = y_pred.astype(float)
    
    formatted_name = format_label(target_name)
    
    ax.scatter(y_true_np, y_pred_np, alpha=0.7)
    ax.plot([y_true_np.min(), y_true_np.max()], [y_true_np.min(), y_true_np.max()], color="red", linestyle="--")
    ax.set_title(f"Actual vs Predicted {formatted_name}")
    ax.set_xlabel(f"Actual {formatted_name}")
    ax.set_ylabel(f"Predicted {formatted_name}")
    fig.tight_layout()
    return render_image(fig)


# ------------------------------------------------------------
# NEW: Feature Importance Endpoint
# ------------------------------------------------------------
@app.post("/feature_importance")
def feature_importance(request: TrainRequest) -> dict[str, Any]:
    from sklearn.feature_selection import mutual_info_regression, mutual_info_classif
    
    if request.session_id not in dataset_cache:
        raise HTTPException(status_code=404, detail="Session ID not found")

    df = dataset_cache[request.session_id]

    try:
        X, y = prepare_features(df, request.target_column)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))

    if X.shape[1] == 0:
        raise HTTPException(status_code=400, detail="No features available for importance analysis.")

    # --- 1. Mutual Information ---
    if request.task_type == "regression":
        mi_scores = mutual_info_regression(X, y, random_state=42)
    else:
        mi_scores = mutual_info_classif(X, y, random_state=42)

    # --- 2. Random Forest Importance ---
    if request.task_type == "regression":
        rf = RandomForestRegressor(n_estimators=50, random_state=42)
    else:
        rf = RandomForestClassifier(n_estimators=50, random_state=42)

    rf.fit(X, y)
    rf_scores = rf.feature_importances_

    # --- 3. Group scores back to original column names ---
    original_names = {}
    for col in X.columns:
        if "_" in col:
            base = col.split("_")[0]
            if base in df.columns:
                original_names[col] = base
            else:
                original_names[col] = col
        else:
            original_names[col] = col

    grouped_mi = {}
    grouped_rf = {}
    for col, mi, rf_score in zip(X.columns, mi_scores, rf_scores):
        base_name = original_names.get(col, col)
        grouped_mi[base_name] = grouped_mi.get(base_name, 0) + abs(mi)
        grouped_rf[base_name] = grouped_rf.get(base_name, 0) + abs(rf_score)

    max_mi = max(grouped_mi.values()) if grouped_mi else 1
    max_rf = max(grouped_rf.values()) if grouped_rf else 1

    result = []
    for col in grouped_mi:
        mi_norm = (grouped_mi[col] / max_mi) * 100 if max_mi > 0 else 0
        rf_norm = (grouped_rf[col] / max_rf) * 100 if max_rf > 0 else 0
        combined = (mi_norm + rf_norm) / 2

        recommended = combined > 15
        reason = ""
        if not recommended:
            if "id" in col.lower() or "ID" in col:
                reason = "Likely a unique identifier (low predictive power)"
            elif combined < 5:
                reason = "Very low predictive power (consider dropping)"
            else:
                reason = "Low predictive power (may not improve model)"

        result.append({
            "column": col,
            "mi_score": round(mi_norm, 2),
            "rf_score": round(rf_norm, 2),
            "combined_score": round(combined, 2),
            "recommended": recommended,
            "reason": reason
        })

    result.sort(key=lambda x: x["combined_score"], reverse=True)

    return {"feature_importance": result}


# ------------------------------------------------------------
# UPDATED: /train endpoint with split_info and dynamic plot labels
# ------------------------------------------------------------
@app.post("/train")
def train(request: TrainRequest) -> dict[str, Any]:
    if request.session_id not in dataset_cache:
        raise HTTPException(status_code=404, detail="Session ID not found")

    # Validate model/task compatibility
    if request.task_type not in TASK_MODEL_MAP:
        raise HTTPException(
            status_code=400,
            detail=f"Unknown task type: '{request.task_type}'. Allowed: {list(TASK_MODEL_MAP.keys())}"
        )

    if request.model_name not in TASK_MODEL_MAP[request.task_type]:
        raise HTTPException(
            status_code=400,
            detail=(
                f"Model '{request.model_name}' is not compatible with task type '{request.task_type}'. "
                f"Allowed models for '{request.task_type}': {TASK_MODEL_MAP[request.task_type]}"
            )
        )

    df = dataset_cache[request.session_id]

    try:
        X, y = prepare_features(df, request.target_column)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # ------------------------------------------------------------
    # NEW: Split Info
    # ------------------------------------------------------------
    split_info = {
        "total_samples": len(X_train) + len(X_test),
        "train_samples": len(X_train),
        "test_samples": len(X_test),
        "train_ratio": round(len(X_train) / (len(X_train) + len(X_test)), 3),
        "test_ratio": round(len(X_test) / (len(X_train) + len(X_test)), 3),
    }

    model_map = {
        "LogisticRegression": LogisticRegression,
        "RandomForestClassifier": RandomForestClassifier,
        "DecisionTreeClassifier": DecisionTreeClassifier,
        "RandomForestRegressor": RandomForestRegressor,
        "LinearRegression": LinearRegression,
        "DecisionTreeRegressor": DecisionTreeRegressor,
        "SVM": SVC,
        "SVR": SVR,
    }

    model = model_map[request.model_name]()

    # ------------------------------------------------------------
    # Capture warnings during fit and predict
    # ------------------------------------------------------------
    warning_messages = []
    with warnings.catch_warnings(record=True) as caught_warnings:
        warnings.simplefilter("always")  # Capture all warnings
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        # Extract warning messages
        for w in caught_warnings:
            warning_messages.append(str(w.message))

    # Also add a custom friendly warning if classification but many unique target values
    if request.task_type == "classification":
        unique_ratio = y.nunique() / len(y)
        if unique_ratio > 0.5:
            warning_messages.append(
                f"Your target column has {y.nunique()} unique values out of {len(y)} samples ({unique_ratio:.1%}). "
                "This might indicate a regression problem. Consider switching to Regression if the values are continuous."
            )

    if request.task_type == "regression":
        mse = mean_squared_error(y_test, y_pred)
        rmse = float(np.sqrt(mse))
        r2 = r2_score(y_test, y_pred)
        # Pass target column name to the plotting function
        image_base64 = render_regression_scatter(y_test, np.array(y_pred), request.target_column)

        return {
            "metrics": {
                "mse": float(mse),
                "rmse": rmse,
                "r2": float(r2),
            },
            "plot": image_base64,
            "warnings": warning_messages,
            "split_info": split_info,
        }
    elif request.task_type == "classification":
        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred, average="weighted", zero_division=0)
        recall = recall_score(y_test, y_pred, average="weighted", zero_division=0)
        f1 = f1_score(y_test, y_pred, average="weighted", zero_division=0)
        # Pass target column name to the plotting function
        image_base64 = render_confusion_matrix(y_test, np.array(y_pred), request.target_column)

        return {
            "metrics": {
                "accuracy": float(accuracy),
                "precision": float(precision),
                "recall": float(recall),
                "f1": float(f1),
            },
            "plot": image_base64,
            "warnings": warning_messages,
            "split_info": split_info,
        }
    else:
        raise HTTPException(status_code=400, detail=f"Unknown task type: {request.task_type}")