# 🤖 AutoML-Lite

## Live Demo

**Frontend (GitHub Pages):**  
🔗 [https://Rishad45-dot.github.io/automl-lite/](https://Rishad45-dot.github.io/automl-lite/)

**Backend:** Runs locally – see installation instructions below.

---

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-009688?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.5+-F7931E?style=flat&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-F7DF1E?style=flat&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 📋 Table of Contents

- [Overview](#overview)
- [Functional Requirements](#functional-requirements)
- [Key Features](#key-features)
- [Tech Stack](#tech-stack)
- [Installation & Setup](#installation--setup)
- [Usage Guide](#usage-guide)
- [Project Structure](#project-structure)
- [Responsible AI Alignment](#responsible-ai-alignment)
- [Limitations & Future Work](#limitations--future-work)
- [Deliverables](#deliverables)
- [License](#license)
- [Acknowledgements](#acknowledgements)

---

## 📖 Overview

**AutoML-Lite** is a **locally-runnable, privacy-first** machine learning web application that allows users to:

- Upload CSV datasets **without sending data to the cloud**.
- Automatically detect headers, column types, and task types.
- Train and evaluate machine learning models with a clean, intuitive interface.
- Generate descriptive statistics, evaluation metrics, and visualizations.

Built with **Responsible AI** principles: **Privacy by Design**, **Transparency**, **Explainability**, and **Human Oversight**.

---

## 📋 Functional Requirements

### 1. Data Handling & Preview

| Requirement | Implementation |
| :--- | :--- |
| **Upload Interface** | ✅ Clean drag-and-drop or click-to-upload UI for CSV files. |
| **Validation** | ✅ Error handling for non-CSV file types with user feedback. |
| **Data Preview** | ✅ Displays the first five rows of the uploaded dataset. |

### 2. Intelligent Configuration

| Requirement | Implementation |
| :--- | :--- |
| **Header Detection** | ✅ Auto-detects CSV headers; manual toggle available for user correction. |
| **Target Selection** | ✅ Defaults to the last column; dropdown menu for manual selection. |
| **Task Identification** | ✅ Automatically determines Classification or Regression based on target column data type; user can override. |

### 3. Analytics & Model Training

| Requirement | Implementation |
| :--- | :--- |
| **Descriptive Statistics** | ✅ Dedicated feature displays mean, standard deviation, and percentiles (min, 25%, 50%, 75%, max). |
| **Model Selection (Regression)** | ✅ Linear Regression, Random Forest Regressor, SVR. |
| **Model Selection (Classification)** | ✅ Logistic Regression, Random Forest Classifier, SVM. |
| **Training Execution** | ✅ 80/20 train-test split with fixed random seed. |
| **Evaluation Metrics** | ✅ MSE, RMSE, R² (Regression); Accuracy, Precision, Recall, F1 (Classification). |
| **Visualizations** | ✅ Confusion Matrix (Classification); Actual vs. Predicted plots (Regression). |

---

## ✨ Key Features

### 🔐 Privacy & Data Handling
- **100% Local Processing** – Data stays on your machine. No cloud uploads.
- **Smart Header Detection** – Auto-detects CSV headers with manual override.
- **Instant Data Preview** – First 5 rows displayed immediately after upload.
- **File Validation** – Only `.csv` files are accepted; clear error messages for invalid files.

### 🧠 Intelligent Configuration
- **Auto Task Detection** – Detects if the target column is classification or regression.
- **Dynamic Model Selection** – Models update based on task type:
  - **Regression:** Linear Regression, Random Forest Regressor, SVR.
  - **Classification:** Logistic Regression, Random Forest Classifier, SVM.
- **Target Selection** – Defaults to the last column; dropdown for manual selection.

### 📊 Model Training & Analytics
- **80/20 Train-Test Split** – Reproducible with fixed random seed (`random_state=42`).
- **Descriptive Statistics** – Mean, standard deviation, and percentiles (min, 25%, 50%, 75%, max) for the target column.
- **Evaluation Metrics**:
  - **Regression:** MSE, RMSE, R² Score.
  - **Classification:** Accuracy, Precision, Recall, F1 Score.
- **Dynamic Visualizations**:
  - **Regression:** Actual vs. Predicted scatter plot with target column in labels.
  - **Classification:** Confusion Matrix with target column in title.
- **Split Info** – Displays total, training, and testing sample counts with percentages.

### 🔎 Explainability & Fairness
- **Feature Importance** – Combines Mutual Information and Random Forest scores, grouped by original column names.
- **Intelligent Warnings** – Alerts users to mismatches (e.g., classification on continuous data).
- **Transparent Metrics** – Human-readable descriptions (e.g., "MSE – lower is better").

### 🎨 User Experience
- **Compact, Modern UI** – Clean design with responsive layout.
- **Auto-Scroll** – Automatically scrolls to results after training or statistics load.
- **Training Card** – Dedicated card below statistics shows the current training goal and allows one-click training.

---

## 🛠 Tech Stack

| Layer | Technology |
| :--- | :--- |
| **Backend** | Python 3.10+, FastAPI, Uvicorn |
| **ML & Data** | Pandas, NumPy, Scikit-learn |
| **Visualization** | Matplotlib |
| **Frontend** | HTML5, CSS3, Vanilla JavaScript (ES6+) |
| **Deployment** | GitHub Pages (frontend), local server (backend) |

---

## 🚀 Installation & Setup

### Prerequisites

Before you begin, ensure you have the following installed on your machine:

| Requirement | Description | How to Check | Why You Need It |
| :--- | :--- | :--- | :--- |
| **Python 3.10+** | The programming language used for the backend. | Run `python --version` or `python3 --version` in your terminal. | The backend is written in Python. Without it, nothing works. |
| **pip** | Python package manager (comes with Python). | Run `pip --version` in your terminal. | Used to install all the required Python packages. |
| **Modern Web Browser** | Chrome, Edge, Firefox, or Safari (latest version recommended). | – | To open and interact with the frontend interface. |
| **Git** (optional) | Version control system to clone the repository. | Run `git --version` in your terminal. | Required only if you want to clone the repository. You can also download the ZIP file. |

---

### 1. Clone or Download the Repository

**Option A: Clone with Git (Recommended)**

Open your terminal and run:

```bash
git clone https://github.com/Rishad45-dot/automl-lite.git
cd automl-lite