# 🤖 AutoML-Lite

**A locally runnable HTML-based application that allows users to upload CSV files, preview data, and run basic machine learning models using a Python backend.**

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-009688?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.5+-F7931E?style=flat&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 📖 Overview

**AutoML-Lite** is a Machine Learning Website with AI copilot:

- Upload CSV datasets **locally** (no cloud uploads – your data never leaves your machine).
- Automatically detect headers, column types, and task type (classification/regression).
- Train machine learning models (Linear Regression, Random Forest, SVR, Logistic Regression, SVM).
- Evaluate models with descriptive metrics and dynamic visualizations.
- Audit models for feature importance and potential bias.


<h1 style="font-size: 3rem; text-align: center; background: linear-gradient(135deg, #6366f1, #8b5cf6); color: white; padding: 1rem; border-radius: 12px;">
Built for <strong>Resp AI Summer School Project</strong>.
</h1>

---

## ✨ Key Features

### 🔐 Privacy & Data Handling
- **100% Local Processing** – Data stays on your machine.
- **Smart Header Detection** – Auto-detects CSV headers with manual override.
- **Instant Data Preview** – First 5 rows displayed immediately.

### 🧠 Intelligent Configuration
- **Auto Task Detection** – Detects if the target is classification or regression.
- **Dynamic Model Selection** – Models update based on task type:
  - *Regression:* Linear, Random Forest, SVR.
  - *Classification:* Logistic, Random Forest, SVM.

### 📊 Model Training & Analytics
- **80/20 Train-Test Split** – Reproducible with fixed random seed.
- **Descriptive Statistics** – Mean, std, and percentiles (min, 25%, 50%, 75%, max) for the target.
- **Evaluation Metrics**:
  - *Regression:* MSE, RMSE, R² Score.
  - *Classification:* Accuracy, Precision, Recall, F1 Score.
- **Dynamic Visualizations**:
  - *Regression:* Actual vs Predicted (with target column in labels).
  - *Classification:* Confusion Matrix (with target column in title).

### 🔎 Explainability & Fairness
- **Feature Importance** – Combines Mutual Information and Random Forest scores.
- **Intelligent Warnings** – Alerts users to mismatches (e.g., classification on continuous data).
- **Transparent Metrics** – Human-readable descriptions (e.g., "MSE – lower is better").

---

## 🛠 Tech Stack

| Layer | Technology |
| :--- | :--- |
| **Backend** | Python 3.10+, FastAPI, Uvicorn |
| **ML & Data** | Pandas, NumPy, Scikit-learn |
| **Visualization** | Matplotlib |
| **Frontend** | HTML5, CSS3, Vanilla JavaScript |

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.10+ installed.
- A modern web browser (Chrome, Edge, Firefox).

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/automl-lite.git
cd automl-lite
