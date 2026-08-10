# AutoML-Lite

**A privacy-first, locally executed automated machine learning platform for tabular data.**

> AutoML-Lite is a full-stack web application that enables non-expert users to upload CSV datasets and obtain trained, evaluated machine learning models — with all data processing confined to the local machine. No data ever leaves the user's environment.

## Live Demo

**Frontend (hosted on GitHub Pages):** [https://Rishad45-dot.github.io/automl-lite/](https://Rishad45-dot.github.io/automl-lite/)

**Backend:** self-hosted — runs locally on the user's machine. See [Installation & Setup](#installation--setup).

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-009688?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.5+-F7931E?style=flat&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-F7DF1E?style=flat&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## Table of Contents

1. [Overview](#overview)
2. [Architecture](#architecture)
3. [Functional Requirements](#functional-requirements)
4. [Key Features](#key-features)
5. [Machine Learning Pipeline](#machine-learning-pipeline)
6. [Tech Stack](#tech-stack)
7. [API Reference](#api-reference)
8. [Installation & Setup](#installation--setup)
9. [Usage Guide](#usage-guide)
10. [Project Structure](#project-structure)
11. [Responsible AI Alignment](#responsible-ai-alignment)
12. [Limitations & Future Work](#limitations--future-work)
13. [Deliverables](#deliverables)
14. [License](#license)
15. [Acknowledgements](#acknowledgements)

---

## Overview

AutoML-Lite is a **locally-runnable, privacy-first** machine learning web application designed for users who need accessible model training without exposing sensitive data to cloud services. The platform provides an end-to-end workflow: CSV ingestion, automatic schema inference, intelligent task detection, configurable model training, quantitative evaluation, and explainability analysis — all exposed through a clean, responsive single-page interface.

The system is engineered around four core **Responsible AI** principles:

| Principle | Implementation |
| :--- | :--- |
| **Privacy by Design** | All data processing occurs in-memory on the local backend; no external storage, telemetry, or cloud transmission. |
| **Transparency** | Every decision the system makes — header detection, task inference, feature encoding — is exposed to the user with a manual override. |
| **Explainability** | Feature importance is computed via a hybrid Mutual Information + Random Forest scoring scheme, aggregated back to human-readable original column names. |
| **Human Oversight** | Users retain control at every stage: header toggle, target selection, task override, and model selection. |

---

## Architecture

AutoML-Lite follows a decoupled client–server architecture. The frontend is a static, dependency-free single-page application served via GitHub Pages; the backend is an asynchronous Python API serving JSON over HTTP.

```
┌──────────────────────────────┐        ┌──────────────────────────────────────────┐
│  Frontend (GitHub Pages)     │        │  Backend (FastAPI / Uvicorn)             │
│                              │  HTTP  │                                          │
│  • CSV upload (fetch API)    │ ─────▶ │  /upload      schema inference           │
│  • Configuration controls    │ ◀───── │  /stats       descriptive statistics    │
│  • Results rendering         │  POST  │  /train       model training & metrics  │
│  • Plot display (base64 PNG) │ ◀───── │  /feature_importance  explainability   │
└──────────────────────────────┘        │                                          │
                                        │  In-memory DataFrame cache (session-id)    │
                                        │  Scikit-learn estimators                 │
                                        └──────────────────────────────────────────┘
                                            Runs entirely on the user's machine
```

Session state is managed through a UUID-keyed in-memory cache on the backend, avoiding any persistent storage. Large outputs (confusion matrices, regression scatter plots) are rendered server-side with Matplotlib and transmitted as base64-encoded PNG payloads, keeping the frontend free of plotting dependencies.

---

## Functional Requirements

### 1. Data Handling & Preview

| Requirement | Implementation |
| :--- | :--- |
| **Upload Interface** | Drag-and-drop and click-to-upload with an accessible fallback; immediate client-side feedback. |
| **Validation** | MIME and extension guard — only `.csv` files are accepted, with descriptive error messages for rejected uploads. |
| **Data Preview** | First five rows rendered immediately upon successful upload for rapid sanity checking. |

### 2. Intelligent Configuration

| Requirement | Implementation |
| :--- | :--- |
| **Header Detection** | Heuristic inference: a header is detected when the first row is fully string-typed and the second row contains at least one numeric cell. Fully numeric first rows are treated as headerless. A manual toggle lets users override the inference. |
| **Target Selection** | Defaults to the last column; a dropdown allows explicit manual selection. |
| **Task Identification** | Automatic task inference from the target column's dtype: boolean, string, categorical, or numeric columns with ≤10 unique values are classified as **classification**; all other numeric columns are treated as **regression**. Users may override the detected task. |

### 3. Analytics & Model Training

| Requirement | Implementation |
| :--- | :--- |
| **Descriptive Statistics** | Mean, standard deviation, and percentiles (min, 25%, 50%, 75%, max) computed on the target column, with an explicit count of valid samples. |
| **Model Selection (Regression)** | Linear Regression, Random Forest Regressor, Decision Tree Regressor, SVR. |
| **Model Selection (Classification)** | Logistic Regression, Random Forest Classifier, Decision Tree Classifier, SVM. |
| **Model–Task Guard** | Strict mapping enforcement: classification-only models are rejected for regression tasks and vice versa, with actionable error messages. |
| **Training Execution** | Deterministic 80/20 train–test split (`random_state=42`) for reproducibility. |
| **Evaluation Metrics** | MSE, RMSE, R² (regression); accuracy, precision, recall, F1 with weighted averaging (classification). |
| **Visualizations** | Confusion matrix (classification); actual-vs-predicted scatter with reference diagonal (regression); target column name embedded in plot labels. |
| **Split Reporting** | Total, training, and test sample counts with ratios displayed alongside metrics. |

---

## Key Features

### Privacy & Data Handling

Data is processed **100% locally** — nothing is transmitted beyond the user's own machine. Schema inference auto-detects CSV headers with a manual override, and the first five rows are previewed immediately after upload. File validation enforces the `.csv` contract with clear user-facing error messages.

### Intelligent Configuration

Task detection reads the target column's dtype and cardinality to select between classification and regression, and the model picker updates dynamically to present only task-compatible estimators. An explicit `TASK_MODEL_MAP` enforces this compatibility at the API layer, preventing meaningless model/task combinations before training begins.

### Model Training & Analytics

Training is executed with a fixed random seed for reproducibility, and results are presented as both quantitative metrics and rendered visualizations. The platform additionally emits **system warnings** captured during fit/predict (e.g., non-convergence of solvers), and heuristically warns when a classification target carries an excessively high unique-value ratio — a strong signal that the problem is better posed as regression.

### Explainability & Fairness

Feature importance is computed through a **hybrid scoring pipeline**: per-feature Mutual Information (MI regression/MI classification, `random_state=42`) and Random Forest Gini importances (50-estimator probe model) are normalized to a 0–100 scale, averaged, and — critically — **grouped back to the user's original column names** so that one-hot-expanded dummies do not fragment the explanation. Features scoring below the 15-point threshold receive actionable guidance (e.g., "Likely a unique identifier (low predictive power)").

### User Experience

The interface uses a compact, responsive layout with automatic scrolling to newly computed results, a dedicated training card that restates the current training objective before one-click execution, and human-readable metric annotations (e.g., "MSE — lower is better").

---

## Machine Learning Pipeline

The backend implements a robust preprocessing pipeline before any estimator is fitted:

1. **Target validation** — the target column is validated for non-empty content; rows with missing targets are excluded.
2. **Feature isolation** — the target column is separated; an empty feature set raises a clear error.
3. **Type normalization** — `datetime64` columns are stringified to preserve temporal information through encoding.
4. **One-hot encoding** — all non-numeric columns are expanded via `pd.get_dummies` (no dropped baseline, preserving interpretability).
5. **Numeric verification** — a final pass confirms every feature column is numeric; otherwise a pinpointed error names the offending column and its sample value.

Evaluation proceeds on the held-out 20% split. Classification metrics use **weighted averaging** (`zero_division=0`) to remain well-defined under class imbalance; regression metrics include RMSE alongside MSE for scale-interpretable error reporting.

---

## Tech Stack

| Layer | Technology |
| :--- | :--- |
| **Backend** | Python 3.10+, FastAPI, Uvicorn (ASGI) |
| **ML & Data** | Pandas, NumPy, Scikit-learn |
| **Visualization** | Matplotlib (server-side, Agg backend) |
| **Frontend** | HTML5, CSS3, Vanilla JavaScript (ES6+) — zero build tooling |
| **Hosting** | GitHub Pages (frontend, static); local host (backend) |
| **API Contract** | REST over JSON; binary plots as base64-encoded PNG |

---

## API Reference

The backend exposes four endpoints. All JSON bodies use the shared `TrainRequest` schema.

```
TrainRequest {
  session_id:      string   // UUID returned by /upload
  target_column:   string   // column name to predict
  task_type:       "classification" | "regression"
  model_name:      string   // see TASK_MODEL_MAP
}
```

| Endpoint | Method | Description |
| :--- | :--- | :--- |
| `/` | `GET` | Health check — `{"message": "Backend is running"}`. |
| `/upload` | `POST` | Accepts a multipart CSV (`file`, optional `has_header` boolean). Returns `session_id`, `columns`, a five-row `preview`, `has_header_guess`, `detected_task`, and the suggested `target_column`. |
| `/stats` | `GET` | Query params `session_id` and optional `target_column`. Returns descriptive statistics for a numeric target. |
| `/train` | `POST` | `TrainRequest`. Trains the requested model and returns `metrics`, `plot` (base64 PNG), `warnings[]`, and `split_info`. |
| `/feature_importance` | `POST` | `TrainRequest`. Returns per-column MI, RF, and combined importance scores with recommendations. |

---

## Installation & Setup

### Prerequisites

| Requirement | Description | How to Check | Why You Need It |
| :--- | :--- | :--- | :--- |
| **Python 3.10+** | Runtime for the backend. | `python --version` or `python3 --version` | The backend is written in Python; without it, nothing works. |
| **pip** | Python package manager (ships with Python). | `pip --version` | Installs all required Python packages. |
| **Modern Web Browser** | Chrome, Edge, Firefox, or Safari (latest recommended). | — | Renders and interacts with the frontend interface. |
| **Git** (optional) | Version control to clone the repository. | `git --version` | Required only for cloning; a ZIP download works equally well. |

### 1. Clone or Download the Repository

**Option A: Clone with Git (Recommended)**

```bash
git clone https://github.com/Rishad45-dot/automl-lite.git
cd automl-lite
```

**Option B: Download as ZIP**

Download the repository ZIP from GitHub and extract it to a local directory.

### 2. Install Backend Dependencies

```bash
pip install fastapi uvicorn pandas numpy scikit-learn matplotlib python-multipart
```

### 3. Start the Backend Server

```bash
python -m uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`. Verify with:

```bash
curl http://127.0.0.1:8000/
# {"message": "Backend is running"}
```

### 4. Open the Frontend

Open the demo URL in your browser — or open `index.html` locally. The frontend points at the local backend automatically via the CORS-enabled API.

---

## Usage Guide

1. **Upload** — drag a `.csv` file onto the upload zone. A preview of the first five rows appears along with the detected header setting, detected task, and suggested target column.
2. **Configure** — review the auto-detected settings; override the header flag, target column, or task type as needed.
3. **Explore** — click **Get Statistics** to view the target column's descriptive statistics.
4. **Train** — select a task-compatible model and click **Train**. The platform runs the 80/20 split, fits the model, and renders metrics, split info, warnings, and the evaluation plot.
5. **Explain** — click **Feature Importance** to see which input columns drive predictions, with per-feature MI and RF scores and drop/keep recommendations.

> **Tip:** For classification tasks, ensure the target column is categorical (string, boolean, or numeric with ≤10 unique values). For regression, the target should be a genuinely continuous numeric column. If the platform suggests switching tasks, it is usually worth listening.

---

## Project Structure

```
automl-lite/
├── index.html            # Frontend SPA (served via GitHub Pages)
├── style.css             # Styling
├── script.js             # Frontend logic (fetch API, DOM rendering)
├── main.py               # FastAPI backend (ML pipeline, API endpoints)
├── requirements.txt      # Python dependencies
└── README.md             # This document
```

---

## Responsible AI Alignment

| Dimension | Practice |
| :--- | :--- |
| **Privacy** | Local-only execution; no network egress beyond the local loopback; no logging of dataset contents. |
| **Transparency** | All auto-inferences (header, task, target) are surfaced and overridable; training warnings are surfaced verbatim. |
| **Explainability** | Hybrid MI + Random Forest feature importance, aggregated to original column names with plain-language recommendations. |
| **Human Oversight** | Manual overrides at header, target, and task level; model selection is always user-initiated. |
| **Reproducibility** | Fixed `random_state=42` across splits and stochastic estimators. |

---

## Limitations & Future Work

**Current limitations:**

- The backend holds uploaded datasets in memory (per-session cache), which bounds dataset size by available RAM.
- Preprocessing is limited to one-hot encoding; no scaling, imputation strategy selection, or polynomial feature generation is exposed.
- Target column defaults to the last column, mirroring the legacy dataset format; manual selection mitigates this.
- Hyperparameters are fixed at scikit-learn defaults; no grid search or cross-validation is offered.

**Planned extensions:**

- Sparse-matrix support for high-cardinality categorical features.
- K-fold cross-validation with aggregated metrics.
- Model persistence and prediction endpoints for new data.
- Additional estimators (gradient boosting, k-NN) and class-imbalance handling (SMOTE, class weights).

---

## Deliverables

| Deliverable | Description |
| :--- | :--- |
| `index.html`, `style.css`, `script.js` | Zero-dependency frontend SPA |
| `main.py` | FastAPI backend implementing the full ML pipeline |
| Live demo | Frontend hosted on GitHub Pages; backend self-hosted |

---

## License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## Acknowledgements

- [Scikit-learn](https://scikit-learn.org/) — machine learning estimators and metrics
- [FastAPI](https://fastapi.tiangolo.com/) — high-performance async API framework
- [Pandas](https://pandas.pydata.org/) / [NumPy](https://numpy.org/) — data manipulation
- [Matplotlib](https://matplotlib.org/) — evaluation visualizations
- [GitHub Pages](https://pages.github.com/) — static frontend hosting
