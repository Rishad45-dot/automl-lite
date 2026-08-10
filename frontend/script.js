const fileInput = document.getElementById("csvFile");
const uploadBtn = document.getElementById("uploadBtn");
const targetSelect = document.getElementById("targetColumn");
const hasHeaderSelect = document.getElementById("hasHeader");
const taskTypeRadios = document.querySelectorAll('input[name="taskType"]');
const modelSelect = document.getElementById("modelSelect");
const modelSelectNew = document.getElementById("modelSelectNew");
const previewTableHead = document.querySelector("#previewTable thead");
const previewTableBody = document.querySelector("#previewTable tbody");
const uploadStatus = document.getElementById("uploadStatus");
const statsBtn = document.getElementById("statsBtn");
const trainBtn = document.getElementById("trainBtn");
const trainBtnNew = document.getElementById("trainBtnNew");
const statsTableHead = document.querySelector("#statsTable thead");
const statsTableBody = document.querySelector("#statsTable tbody");
const metricsOutput = document.getElementById("metricsOutput");
const plotContainer = document.getElementById("plotContainer");
const trainingDescription = document.getElementById("trainingDescription");

const state = {
  sessionId: null,
  columns: [],
  previewRows: [],
  detectedTask: "classification",
  filename: null,
};

// ------------------------------------------------------------
// RENDER WARNINGS
// ------------------------------------------------------------
function renderWarnings(warnings) {
  let warningsContainer = document.getElementById("warningsOutput");
  if (!warningsContainer) {
    warningsContainer = document.createElement("div");
    warningsContainer.id = "warningsOutput";
    warningsContainer.className = "warnings-output";
    metricsOutput.parentNode.insertBefore(warningsContainer, metricsOutput.nextSibling);
  }

  if (!warnings || warnings.length === 0) {
    warningsContainer.innerHTML = "";
    warningsContainer.style.display = "none";
    return;
  }

  const items = warnings.map((w) => `<div class="warning-banner">⚠️ ${w}</div>`).join("");
  warningsContainer.innerHTML = items;
  warningsContainer.style.display = "block";
}

// ------------------------------------------------------------
// DROPDOWN POPULATORS
// ------------------------------------------------------------
function updateModelDropdown(taskType) {
  const modelOptions =
    taskType === "regression"
      ? [
          { value: "LinearRegression", label: "Linear Regression" },
          { value: "RandomForestRegressor", label: "Random Forest Regressor" },
          { value: "SVR", label: "SVR" },
        ]
      : [
          { value: "LogisticRegression", label: "Logistic Regression" },
          { value: "RandomForestClassifier", label: "Random Forest Classifier" },
          { value: "SVM", label: "SVM" },
        ];

  modelSelect.innerHTML = "";
  modelOptions.forEach((option) => {
    const opt = document.createElement("option");
    opt.value = option.value;
    opt.textContent = option.label;
    modelSelect.appendChild(opt);
  });
  // Also update the new dropdown
  updateModelDropdownNew(taskType);
}

function updateModelDropdownNew(taskType) {
  const modelOptions =
    taskType === "regression"
      ? [
          { value: "LinearRegression", label: "Linear Regression" },
          { value: "RandomForestRegressor", label: "Random Forest Regressor" },
          { value: "SVR", label: "SVR" },
        ]
      : [
          { value: "LogisticRegression", label: "Logistic Regression" },
          { value: "RandomForestClassifier", label: "Random Forest Classifier" },
          { value: "SVM", label: "SVM" },
        ];

  modelSelectNew.innerHTML = "";
  modelOptions.forEach((option) => {
    const opt = document.createElement("option");
    opt.value = option.value;
    opt.textContent = option.label;
    modelSelectNew.appendChild(opt);
  });
  // Keep value in sync with top
  modelSelectNew.value = modelSelect.value;
}

// ------------------------------------------------------------
// DESCRIPTION GENERATOR
// ------------------------------------------------------------
function generateDescription() {
  const taskType = document.querySelector('input[name="taskType"]:checked')?.value || "classification";
  const modelNameRaw = modelSelect.value || "LinearRegression";
  const target = targetSelect.value || "target";
  const features = state.columns.filter(col => col !== target);
  const filename = state.filename || "the uploaded dataset";

  // Format model name (e.g., "LinearRegression" → "Linear Regression")
  const modelDisplay = modelNameRaw
    .replace(/([A-Z])/g, " $1")
    .replace(/^./, str => str.toUpperCase())
    .replace("S V R", "SVR")
    .replace("S V M", "SVM")
    .replace("R F", "RF")
    .trim();

  const verb = taskType === "regression" ? "predict" : "classify";
  const targetType = taskType === "regression" ? "continuous values" : "categories";

  let featureList = "all available features";
  if (features.length === 1) {
    featureList = `1 feature: **"${features[0]}"**`;
  } else if (features.length > 1 && features.length <= 5) {
    featureList = features.join(", ");
  } else if (features.length > 5) {
    featureList = features.slice(0, 5).join(", ") + " and others";
  }

  return `Training a **${modelDisplay}** model to **${verb}** the target variable **"${target}"** (${targetType}) using ${featureList} from dataset **"${filename}"**.`;
}

// ------------------------------------------------------------
// UPDATE TRAINING CARD
// ------------------------------------------------------------
function updateTrainingCard() {
  // Update the description
  trainingDescription.innerHTML = generateDescription();

  // Sync the new card's dropdown with the top card
  modelSelectNew.value = modelSelect.value;

  // Sync the new card's task radios with the top card
  const topTaskType = document.querySelector('input[name="taskType"]:checked')?.value || "classification";
  // The radios share the same name, so they are automatically in sync.
  // Just ensure the dropdowns match.
  updateModelDropdownNew(topTaskType);
}

// ------------------------------------------------------------
// UI FUNCTIONS
// ------------------------------------------------------------
function populateTargetDropdown(columns) {
  targetSelect.innerHTML = "";
  columns.forEach((column) => {
    const option = document.createElement("option");
    option.value = column;
    option.textContent = column;
    targetSelect.appendChild(option);
  });
}

function populatePreviewTable(rows) {
  previewTableHead.innerHTML = "";
  previewTableBody.innerHTML = "";

  if (!rows.length) {
    previewTableBody.innerHTML = '<tr><td colspan="1">No preview data available.</td></tr>';
    return;
  }

  const headers = Object.keys(rows[0]);
  const headerRow = document.createElement("tr");
  headers.forEach((header) => {
    const th = document.createElement("th");
    th.textContent = header;
    headerRow.appendChild(th);
  });
  previewTableHead.appendChild(headerRow);

  rows.forEach((row) => {
    const tr = document.createElement("tr");
    headers.forEach((header) => {
      const td = document.createElement("td");
      const value = row[header];
      td.textContent = value === null || value === undefined ? "" : String(value);
      tr.appendChild(td);
    });
    previewTableBody.appendChild(tr);
  });
}

// ------------------------------------------------------------
// UPDATED: renderMetrics with splitInfo
// ------------------------------------------------------------
function renderMetrics(metrics, modelName, splitInfo) {
  const metricEntries = Object.entries(metrics || {});
  if (!metricEntries.length) {
    metricsOutput.innerHTML = "No metrics available.";
    return;
  }

  const metricDefinitions = {
    mse: { label: "MSE", desc: "Mean Squared Error (lower is better)" },
    rmse: { label: "RMSE", desc: "Root Mean Squared Error (lower is better)" },
    r2: { label: "R² Score", desc: "Proportion of variance explained (closer to 1 is better)" },
    accuracy: { label: "Accuracy", desc: "Overall correctness (higher is better)" },
    precision: { label: "Precision", desc: "Exactness of positive predictions (higher is better)" },
    recall: { label: "Recall", desc: "Completeness of positive predictions (higher is better)" },
    f1: { label: "F1 Score", desc: "Harmonic mean of Precision & Recall (higher is better)" },
  };

  const items = metricEntries
    .map(([key, value]) => {
      const def = metricDefinitions[key] || { label: key, desc: "" };
      return `
        <div class="metric-item">
          <div class="metric-info">
            <div class="metric-name">${def.label}</div>
            <div class="metric-desc">${def.desc}</div>
          </div>
          <div class="metric-value">${Number(value).toFixed(4)}</div>
        </div>
      `;
    })
    .join("");

  // Build split info HTML if available
  let splitHtml = "";
  if (splitInfo) {
    const total = splitInfo.total_samples || 0;
    const train = splitInfo.train_samples || 0;
    const test = splitInfo.test_samples || 0;
    const trainPct = (splitInfo.train_ratio * 100).toFixed(0);
    const testPct = (splitInfo.test_ratio * 100).toFixed(0);
    splitHtml = `
      <div class="split-info">
        <span>📊 Training: <strong>${train}</strong> samples (${trainPct}%)</span>
        <span>🧪 Testing: <strong>${test}</strong> samples (${testPct}%)</span>
        <span>📦 Total: <strong>${total}</strong> samples</span>
      </div>
    `;
  }

  metricsOutput.innerHTML = `
    <div class="metric-card">
      <div class="metric-header">${modelName || "Model"}</div>
      <div class="metric-grid">${items}</div>
      ${splitHtml}
    </div>
  `;
}

function renderPlot(imageBase64) {
  if (!imageBase64) {
    plotContainer.innerHTML = "No plot generated.";
    return;
  }
  plotContainer.innerHTML = `<img src="data:image/png;base64,${imageBase64}" alt="Training plot" />`;
}

// ------------------------------------------------------------
// UPDATED: populateStatsTable – single row, no histogram
// ------------------------------------------------------------
function populateStatsTable(statsData) {
  statsTableHead.innerHTML = "";
  statsTableBody.innerHTML = "";

  if (!statsData || !statsData.column) {
    statsTableBody.innerHTML = '<tr><td colspan="2">No statistics available for the target column.</td></tr>';
    return;
  }

  const headerRow = document.createElement("tr");
  ["Column", "Mean", "Std", "Min", "25%", "50%", "75%", "Max", "Count"].forEach((header) => {
    const th = document.createElement("th");
    th.textContent = header;
    headerRow.appendChild(th);
  });
  statsTableHead.appendChild(headerRow);

  const tr = document.createElement("tr");
  
  const tdColumn = document.createElement("td");
  tdColumn.textContent = statsData.column;
  tdColumn.style.fontWeight = "bold";
  tr.appendChild(tdColumn);

  const statsKeys = ["mean", "std", "min", "25%", "50%", "75%", "max", "count"];
  statsKeys.forEach((key) => {
    const td = document.createElement("td");
    td.textContent = statsData[key] !== undefined ? Number(statsData[key]).toFixed(4) : "";
    tr.appendChild(td);
  });

  statsTableBody.appendChild(tr);
}

function setTaskType(taskType) {
  state.detectedTask = taskType;
  const selectedRadio = Array.from(taskTypeRadios).find((radio) => radio.value === taskType);
  if (selectedRadio) {
    selectedRadio.checked = true;
  }
  updateModelDropdown(taskType);
  updateTrainingCard();
}

// ------------------------------------------------------------
// FEATURE IMPORTANCE (for the "Analyze Features" button)
// ------------------------------------------------------------
async function analyzeFeatures() {
  if (!state.sessionId) {
    alert("Please upload a dataset first.");
    return;
  }

  const taskType = document.querySelector('input[name="taskType"]:checked')?.value || state.detectedTask;
  const payload = {
    session_id: state.sessionId,
    target_column: targetSelect.value,
    task_type: taskType,
    model_name: modelSelect.value,
  };

  metricsOutput.innerHTML = "Analyzing feature importance...";

  try {
    const response = await fetch("http://127.0.0.1:8000/feature_importance", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });

    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.detail || "Feature analysis failed");
    }

    const features = data.feature_importance || [];
    if (features.length === 0) {
      metricsOutput.innerHTML = "No features available for analysis.";
      return;
    }

    let html = `<div class="metric-card"><div class="metric-header">Feature Importance</div>`;
    html += `<table style="width:100%; font-size:0.85rem; border-collapse:collapse;">`;
    html += `<tr><th>Feature</th><th>Score</th><th>Recommendation</th></tr>`;
    features.forEach(f => {
      const icon = f.recommended ? "✅" : "❌";
      html += `<tr>
        <td style="padding:0.3rem; border-bottom:1px solid #f1f5f9;">${f.column}</td>
        <td style="padding:0.3rem; border-bottom:1px solid #f1f5f9;">${f.combined_score.toFixed(1)}</td>
        <td style="padding:0.3rem; border-bottom:1px solid #f1f5f9;">${icon} ${f.recommended ? "Keep" : f.reason || "Drop"}</td>
      </tr>`;
    });
    html += `</table></div>`;
    metricsOutput.innerHTML = html;
  } catch (error) {
    metricsOutput.innerHTML = error.message || "Feature analysis failed.";
  }
}

// ------------------------------------------------------------
// TRAIN MODEL
// ------------------------------------------------------------
async function trainModel() {
  if (!state.sessionId) {
    metricsOutput.innerHTML = "Upload a dataset first.";
    plotContainer.innerHTML = "No plot generated.";
    renderWarnings([]);
    return;
  }

  const taskType = document.querySelector('input[name="taskType"]:checked')?.value || state.detectedTask;
  const payload = {
    session_id: state.sessionId,
    target_column: targetSelect.value,
    task_type: taskType,
    model_name: modelSelect.value,
  };

  metricsOutput.innerHTML = "Training model...";
  plotContainer.innerHTML = "Generating plot...";
  renderWarnings([]);

  try {
    const response = await fetch("http://127.0.0.1:8000/train", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });

    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.detail || "Training failed");
    }

    // Pass splitInfo to renderMetrics
    renderMetrics(data.metrics || {}, payload.model_name, data.split_info);
    renderPlot(data.plot || "");
    renderWarnings(data.warnings || []);

    // Scroll to metrics
    const metricsPanel = document.querySelector('.metrics-panel');
    if (metricsPanel) {
      metricsPanel.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  } catch (error) {
    metricsOutput.innerHTML = error.message || "Training failed.";
    plotContainer.innerHTML = "No plot generated.";
    renderWarnings([]);
  }
}

// ------------------------------------------------------------
// LOAD STATISTICS (sends target_column to backend)
// ------------------------------------------------------------
async function loadStatistics() {
  if (!state.sessionId) {
    statsTableBody.innerHTML = '<tr><td colspan="9">Upload a dataset first.</td></tr>';
    return;
  }

  try {
    const targetColumn = targetSelect.value;
    const response = await fetch(
      `http://127.0.0.1:8000/stats?session_id=${encodeURIComponent(state.sessionId)}&target_column=${encodeURIComponent(targetColumn)}`
    );
    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.detail || "Failed to load statistics");
    }

    populateStatsTable(data.stats || {});
    const statsCol = document.querySelector('.stats-col');
    if (statsCol) {
      statsCol.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  } catch (error) {
    statsTableBody.innerHTML = `<tr><td colspan="9">${error.message}</td></tr>`;
  }
}

// ------------------------------------------------------------
// UPLOAD DATASET
// ------------------------------------------------------------
async function uploadDataset(file) {
  if (!file) {
    uploadStatus.textContent = "Please choose a CSV file first.";
    return;
  }

  const formData = new FormData();
  formData.append("file", file);
  formData.append("has_header", hasHeaderSelect.value);

  uploadStatus.textContent = "Uploading...";

  try {
    const response = await fetch("http://127.0.0.1:8000/upload", {
      method: "POST",
      body: formData,
    });

    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.detail || "Upload failed");
    }

    state.sessionId = data.session_id;
    state.columns = data.columns || [];
    state.previewRows = data.preview || [];
    state.detectedTask = data.detected_task || "classification";
    state.filename = file.name;

    populateTargetDropdown(state.columns);
    targetSelect.value = data.target_column || state.columns[state.columns.length - 1] || "";

    if (data.has_header_guess !== undefined && data.has_header_guess !== null) {
      hasHeaderSelect.value = String(data.has_header_guess);
    } else {
      hasHeaderSelect.value = "true";
    }

    populatePreviewTable(state.previewRows);
    setTaskType(state.detectedTask);
    updateTrainingCard();

    uploadStatus.textContent = `Uploaded ${file.name}. Session ready.`;
  } catch (error) {
    uploadStatus.textContent = error.message || "An unexpected error occurred.";
  }
}

// ------------------------------------------------------------
// EVENT LISTENERS
// ------------------------------------------------------------
fileInput.addEventListener("change", (event) => {
  const file = event.target.files?.[0];
  uploadDataset(file);
});

uploadBtn.addEventListener("click", () => {
  const file = fileInput.files?.[0];
  uploadDataset(file);
});

// Top card task type radios
taskTypeRadios.forEach((radio) => {
  radio.addEventListener("change", () => {
    if (radio.checked) {
      setTaskType(radio.value);
    }
  });
});

// Sync new card model dropdown with top card
modelSelect.addEventListener("change", () => {
  modelSelectNew.value = modelSelect.value;
  updateTrainingCard();
});

modelSelectNew.addEventListener("change", () => {
  modelSelect.value = modelSelectNew.value;
  updateTrainingCard();
});

// Sync new card radios with top card (they share the same name, so they are already in sync)
// But we need to update description when they change – we can listen to change on all radios
document.querySelectorAll('input[name="taskType"]').forEach((radio) => {
  radio.addEventListener("change", () => {
    if (radio.checked) {
      // Update both cards' model dropdowns to match task type
      updateModelDropdown(radio.value);
      // Also ensure the new dropdown is updated
      updateModelDropdownNew(radio.value);
      // Update description
      updateTrainingCard();
    }
  });
});

statsBtn.addEventListener("click", loadStatistics);
trainBtn.addEventListener("click", trainModel);
trainBtnNew.addEventListener("click", trainModel);

// Feature importance button (if it exists in the HTML)
document.getElementById("featureBtn")?.addEventListener("click", analyzeFeatures);

// Initialize
updateModelDropdown("classification");
populatePreviewTable([]);
populateStatsTable({});
updateTrainingCard();