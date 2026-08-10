# 🤖 AutoML-Lite

## Live Demo

**Frontend (GitHub Pages):**  
🔗 [https://Rishad45-dot.github.io/automl-lite/](https://Rishad45-dot.github.io/automl-lite/)

**Backend:** Runs locally – see [Installation & Setup](#installation--setup) for detailed instructions.

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

**AutoML-Lite** is a **locally-runnable, privacy-first** machine learning web application that enables users to:

- Upload CSV datasets **without sending data to the cloud**.
- Automatically detect headers, column types, and task types.
- Train and evaluate machine learning models through a clean, intuitive interface.
- Generate descriptive statistics, evaluation metrics, and visualizations.

Built with **Responsible AI** principles: **Privacy by Design**, **Transparency**, **Explainability**, and **Human Oversight** in mind.

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

This guide provides step-by-step instructions to get AutoML-Lite running on your local machine.

### Prerequisites

Ensure your system meets the following requirements before proceeding.

| Requirement | Description | How to Verify | Why It's Needed |
| :--- | :--- | :--- | :--- |
| **Python 3.10 or Higher** | The backend is built with Python. | Run `python --version` or `python3 --version` in your terminal. | The core server and ML logic depend on Python. |
| **pip** | The Python package installer. | Run `pip --version` or `pip3 --version`. | Essential for installing project dependencies. |
| **Modern Web Browser** | Chrome, Edge, Firefox, or Safari (latest version). | N/A | To access and interact with the web interface. |
| **Git (Optional)** | For cloning the repository. | Run `git --version`. | Required if you choose to clone the project via Git. You can also download the ZIP file directly. |

### Step 1: Obtain the Source Code

**Option A: Clone with Git (Recommended)**

Open your terminal and run:

```bash
git clone https://github.com/Rishad45-dot/automl-lite.git
cd automl-lite
