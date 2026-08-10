# 🤖 AutoML-Lite
## Live Demo
**Static Frontend (GitHub Pages Deployment):**
🔗 [https://Rishad45-dot.github.io/automl-lite/](https://Rishad45-dot.github.io/automl-lite/)
<<<<<<< HEAD
**Application Backend:** Executes entirely on local infrastructure — full installation and runtime instructions documented below.
=======

**Backend:** Runs locally – see [Installation & Setup](#installation--setup) for detailed instructions.
>>>>>>> 6a6eda38ee27f5238359f10a9d522343c46476ad

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
- [Executive Overview](#executive-overview)
- [Functional & System Requirements](#functional--system-requirements)
- [Core Platform Capabilities](#core-platform-capabilities)
- [Full Technology Stack](#full-technology-stack)
- [Installation & Environment Provisioning](#installation--environment-provisioning)
- [End-to-End User Workflow Guide](#end-to-end-user-workflow-guide)
- [Standardized Project Directory Structure](#standardized-project-directory-structure)
- [Responsible AI Governance Framework](#responsible-ai-governance-framework)
- [System Limitations & Product Roadmap](#system-limitations--product-roadmap)
- [Project Deliverable Inventory](#project-deliverable-inventory)
- [Software License](#software-license)
- [Attributions & Acknowledgements](#attributions--acknowledgements)

---
## 📖 Executive Overview
**AutoML-Lite** is a privacy-preserving, locally executed automated machine learning web application engineered for data practitioners, analysts, and entry-level ML engineers. The platform eliminates reliance on third-party cloud compute and data ingestion pipelines, enabling end-users to conduct end-to-end supervised machine learning workflows entirely on their local workstation.

<<<<<<< HEAD
Key supported workflows include secure CSV dataset ingestion, automated schema inference, supervised task classification detection, standardized model training, quantitative performance benchmarking, and interpretability visualisation generation. The platform adheres to formal Responsible AI design tenets: Privacy-by-Design, algorithmic transparency, model explainability, and human-in-the-loop oversight for all modelling stages.
=======
## 📖 Overview

**AutoML-Lite** is a **locally-runnable, privacy-first** machine learning web application that enables users to:

- Upload CSV datasets **without sending data to the cloud**.
- Automatically detect headers, column types, and task types.
- Train and evaluate machine learning models through a clean, intuitive interface.
- Generate descriptive statistics, evaluation metrics, and visualizations.

Built with **Responsible AI** principles: **Privacy by Design**, **Transparency**, **Explainability**, and **Human Oversight** in mind.
>>>>>>> 6a6eda38ee27f5238359f10a9d522343c46476ad

---
## 📋 Functional & System Requirements
### 1. Dataset Ingestion & Interactive Preview Module
| Functional Requirement | Implementation Status & Technical Details |
| :--- | :--- |
| Standardised File Upload Interface | ✅ Implements dual-input upload paradigm: drag-and-drop zone + click-triggered file selector with responsive, accessible UI components for CSV ingestion. |
| Strict File Type Validation & Error Handling | ✅ Input sanitisation pipeline restricts uploads to `.csv` MIME types only; contextual, human-readable error notifications surface invalid file formats, corrupted datasets, and empty payloads. |
| Real-Time Dataset Preview Rendering | ✅ Post-ingestion low-latency rendering of the first five dataset records to enable rapid schema validation prior to modelling configuration. |

### 2. Automated ML Pipeline Configuration Engine
| Functional Requirement | Implementation Status & Technical Details |
| :--- | :--- |
| Automated Header Row Inference | ✅ Heuristic-based CSV header detection algorithm with user-accessible toggle control to manually override auto-detection results for malformed or headerless datasets. |
| Target Variable Assignment Control | ✅ Default target column mapping set to the final dataset column; dropdown selection component enables explicit manual target feature reassignment. |
| Supervised Task Auto-Classification | ✅ Statistical type inference pipeline auto-detects regression (continuous target) vs. classification (categorical/discrete target) tasks; user override toggle permits manual task reclassification for edge-case datasets. |

### 3. Descriptive Analytics & Model Training Subsystem
| Functional Requirement | Implementation Status & Technical Details |
| :--- | :--- |
| Univariate Descriptive Statistical Reporting | ✅ Dedicated analytics panel computes and displays aggregate statistics: central tendency (mean), dispersion (standard deviation), and quantile metrics (min, 25th, median/50th, 75th, max percentiles) for the designated target feature. |
| Modular Regression Model Library | ✅ Pre-integrated baseline regression estimators: Linear Regression, Random Forest Regressor, Support Vector Regressor (SVR). |
| Modular Classification Model Library | ✅ Pre-integrated baseline classification estimators: Logistic Regression, Random Forest Classifier, Support Vector Machine (SVM). |
| Reproducible Train-Test Dataset Partitioning | ✅ Standardised 80/20 train/test split stratification with fixed static random seed (`random_state=42`) to guarantee fully reproducible training results across execution sessions. |
| Standardised Quantitative Evaluation Metrics | ✅ Regression suite: MSE, RMSE, R² Score; Classification suite: Global Accuracy, Class-wise Precision, Recall, F1-Score. All metrics paired with plain-language interpretive annotations. |
| Dynamic Model Diagnostics Visualisations | ✅ Classification output: Normalised confusion matrix heatmap labelled with target variable metadata; Regression output: Actual vs. Predicted value scatter plot for residual analysis. |

---
## ✨ Core Platform Capabilities
### 🔐 Enterprise-Grade Data Privacy & Secure Ingestion
- **Zero Cloud Data Egress Architecture**: All dataset parsing, feature engineering, model training, and visualisation rendering executes locally on the end-user’s hardware. No raw or derived data payloads are transmitted to external cloud APIs or remote servers.
- **Configurable CSV Header Inference**: Automated schema detection with manual override controls for non-standard CSV formatting.
- **Low-Latency Dataset Sampling Preview**: Instant rendering of top-five dataset records immediately post-upload for rapid data quality validation.
- **Robust Input Sanitisation Layer**: Strict file extension and MIME-type filtering with granular error messaging for invalid, corrupted, or unsupported input payloads.

### 🧠 Automated ML Pipeline Orchestration
- **Statistical Task Inference Engine**: Unsupervised type analysis to auto-distinguish regression and classification modelling tasks without manual user input.
- **Context-Aware Model Selector UI**: Model library dynamically filters to display only estimators compatible with the detected supervised learning task; all baseline algorithms pre-configured with sensible default hyperparameters for rapid prototyping.
- **Flexible Target Variable Selection**: Default mapping to last dataset column with interactive dropdown for custom target feature assignment.

### 📊 Standardised Model Training & Performance Analytics
- **Deterministic Train/Test Partitioning**: Fixed random state ensures identical dataset splits across repeated training runs for reproducible benchmarking.
- **Comprehensive Univariate Target Statistics Panel**: Complete quantile and distribution metrics to enable preliminary target variable quality assessment prior to training.
- **Industry-Standard Evaluation Metric Suites**: Task-aligned quantitative scoring with embedded plain-text definitions to reduce interpretive friction for non-specialist users.
- **Contextualised Diagnostic Visualisations**: Labelled, publication-ready plots for residual and classification error analysis, dynamically titled with active target feature metadata.
- **Dataset Partition Metadata Dashboard**: Real-time display of total record count, training sample volume, test sample volume, and proportional split percentages for audit transparency.

### 🔎 Model Explainability & Algorithmic Governance
- **Multi-Source Feature Importance Ranking**: Hybrid importance calculation combining mutual information statistical scoring and Random Forest feature weight attribution, aggregated and grouped by original input column identifiers for intuitive interpretability.
- **Pre-Execution Data Consistency Guardrails**: Contextual warning notifications alert users to configuration mismatches (e.g., continuous target variable assigned to classification task) to prevent invalid model training workflows.
- **Human-Centric Metric Labelling**: Every quantitative metric includes plain-language guidance (e.g., "MSE: Lower numerical values indicate superior predictive performance") to standardise result interpretation across skill levels.

### 🎨 Production-Grade User Experience & Interface Design
- **Mobile-First Responsive Web UI**: Compact, modular component layout optimised for desktop, laptop, and tablet viewing resolutions.
- **Automated Viewport Scrolling Logic**: Post-computation auto-scroll functionality navigates the UI to newly generated statistical or training result panels to minimise manual user navigation overhead.
- **Modular Training Control Card**: Dedicated, isolated UI component housing training configuration parameters and a single-click execution trigger for streamlined model training initiation.

---
## 🛠 Full Technology Stack
| Architectural Layer | Production Technology Suite |
| :--- | :--- |
| Application Backend API | Python 3.10+, FastAPI 0.115+, Uvicorn ASGI Production Server |
| Data Processing & Machine Learning Core | Pandas, NumPy, Scikit-learn v1.5+ |
| Static Visualisation Rendering | Matplotlib (server-side plot generation, base64 payload delivery to frontend) |
| Client-Side Frontend Interface | HTML5 Semantic Markup, CSS3 Custom Properties, Vanilla ES6+ JavaScript (zero external frontend framework dependencies) |
| Deployment Targets | Static frontend asset hosting via GitHub Pages; backend restricted to local workstation execution only |

---
# 🚀 Installation & Environment Provisioning
This section formalises a reproducible, step-by-step environment setup workflow for Windows, macOS, and Linux operating systems, including pre-flight validation, repository acquisition, dependency provisioning, and backend service initialisation. All commands follow cross-platform best practices with platform-specific callouts where applicable.

## 1. Pre-Flight Prerequisite Validation
Complete the below environment audit before repository deployment to eliminate runtime dependency failures. All listed tooling is mandatory for full platform functionality.

<<<<<<< HEAD
| Prerequisite Component | Formal Description | Validation Command | Criticality Rationale |
| :--- | :--- | :--- | :--- |
| Python 3.10 or Newer Interpreter | Core runtime environment powering the FastAPI backend, data parsing, and machine learning computation layers. | Terminal / Command Prompt:<br>`python --version`<br>macOS/Linux fallback: `python3 --version` | The backend and ML core are natively implemented in Python; incompatible minor/major versions introduce breaking API and library compatibility errors. |
| Python Package Installer (pip) | Official Python package management utility bundled with standard Python 3.10+ distributions, used to resolve and install all third-party dependency libraries. | Terminal / Command Prompt:<br>`pip --version`<br>macOS/Linux fallback: `pip3 --version` | Required to provision the complete ML and API dependency stack; no alternative package managers are officially supported for this project. |
| Standards-Compliant Modern Web Browser | Rendering engine for the static frontend web interface; supports ES6+ JavaScript, modern CSS, and base64 image payload ingestion for visualisation rendering. | N/A (Manual version check via browser "About" menu) | Legacy browsers lack required JavaScript and DOM APIs to execute the full frontend interactive workflow. Recommended releases: Google Chrome, Microsoft Edge, Mozilla Firefox, Apple Safari (latest stable channel builds). |
| Git Version Control System (Optional) | Distributed source control client to clone the remote GitHub repository source code. | Terminal / Command Prompt:<br>`git --version` | Only required for repository cloning workflows. If Git is unavailable, users may download the project source as a compressed ZIP archive directly from the repository GitHub page. |

## 2. Repository Source Code Acquisition
Two officially supported deployment pathways are provided for source code retrieval; the Git clone method is recommended for future project update compatibility.

### Option A: Git Repository Clone (Recommended)
1. Launch your native system terminal (Terminal on macOS/Linux, PowerShell / Command Prompt on Windows).
2. Navigate to a target working directory where the project source will be stored locally (example directory command provided below).
3. Execute the repository clone command to pull the complete source tree from GitHub.
4. Enter the project root directory post-clone completion.
=======
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
>>>>>>> 6a6eda38ee27f5238359f10a9d522343c46476ad

```bash
# Navigate to your preferred project storage directory (example for cross-platform consistency)
cd ~/Projects
# Clone the public source repository
git clone https://github.com/Rishad45-dot/automl-lite.git
<<<<<<< HEAD
# Enter the project root working directory
cd automl-lite

# AutoML-Lite README.md
Copy all content below, create a new file named `README.md` on your local machine, paste everything and save it directly for download/use.
```markdown
# 🤖 AutoML-Lite
## Live Demo
**Static Frontend (GitHub Pages Deployment):**
🔗 [https://Rishad45-dot.github.io/automl-lite/](https://Rishad45-dot.github.io/automl-lite/)
**Application Backend:** Executes entirely on local infrastructure — full installation and runtime instructions documented below.

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
- [Executive Overview](#executive-overview)
- [Functional & System Requirements](#functional--system-requirements)
- [Core Platform Capabilities](#core-platform-capabilities)
- [Full Technology Stack](#full-technology-stack)
- [Installation & Environment Provisioning](#installation--environment-provisioning)
- [End-to-End User Workflow Guide](#end-to-end-user-workflow-guide)
- [Standardized Project Directory Structure](#standardized-project-directory-structure)
- [Responsible AI Governance Framework](#responsible-ai-governance-framework)
- [System Limitations & Product Roadmap](#system-limitations--product-roadmap)
- [Project Deliverable Inventory](#project-deliverable-inventory)
- [Software License](#software-license)
- [Attributions & Acknowledgements](#attributions--acknowledgements)

---
## 📖 Executive Overview
**AutoML-Lite** is a privacy-preserving, locally executed automated machine learning web application engineered for data practitioners, analysts, and entry-level ML engineers. The platform eliminates reliance on third-party cloud compute and data ingestion pipelines, enabling end-users to conduct end-to-end supervised machine learning workflows entirely on their local workstation.

Key supported workflows include secure CSV dataset ingestion, automated schema inference, supervised task classification detection, standardized model training, quantitative performance benchmarking, and interpretability visualisation generation. The platform adheres to formal Responsible AI design tenets: Privacy-by-Design, algorithmic transparency, model explainability, and human-in-the-loop oversight for all modelling stages.

---
## 📋 Functional & System Requirements
### 1. Dataset Ingestion & Interactive Preview Module
| Functional Requirement | Implementation Status & Technical Details |
| :--- | :--- |
| Standardised File Upload Interface | ✅ Implements dual-input upload paradigm: drag-and-drop zone + click-triggered file selector with responsive, accessible UI components for CSV ingestion. |
| Strict File Type Validation & Error Handling | ✅ Input sanitisation pipeline restricts uploads to `.csv` MIME types only; contextual, human-readable error notifications surface invalid file formats, corrupted datasets, and empty payloads. |
| Real-Time Dataset Preview Rendering | ✅ Post-ingestion low-latency rendering of the first five dataset records to enable rapid schema validation prior to modelling configuration. |

### 2. Automated ML Pipeline Configuration Engine
| Functional Requirement | Implementation Status & Technical Details |
| :--- | :--- |
| Automated Header Row Inference | ✅ Heuristic-based CSV header detection algorithm with user-accessible toggle control to manually override auto-detection results for malformed or headerless datasets. |
| Target Variable Assignment Control | ✅ Default target column mapping set to the final dataset column; dropdown selection component enables explicit manual target feature reassignment. |
| Supervised Task Auto-Classification | ✅ Statistical type inference pipeline auto-detects regression (continuous target) vs. classification (categorical/discrete target) tasks; user override toggle permits manual task reclassification for edge-case datasets. |

### 3. Descriptive Analytics & Model Training Subsystem
| Functional Requirement | Implementation Status & Technical Details |
| :--- | :--- |
| Univariate Descriptive Statistical Reporting | ✅ Dedicated analytics panel computes and displays aggregate statistics: central tendency (mean), dispersion (standard deviation), and quantile metrics (min, 25th, median/50th, 75th, max percentiles) for the designated target feature. |
| Modular Regression Model Library | ✅ Pre-integrated baseline regression estimators: Linear Regression, Random Forest Regressor, Support Vector Regressor (SVR). |
| Modular Classification Model Library | ✅ Pre-integrated baseline classification estimators: Logistic Regression, Random Forest Classifier, Support Vector Machine (SVM). |
| Reproducible Train-Test Dataset Partitioning | ✅ Standardised 80/20 train/test split stratification with fixed static random seed (`random_state=42`) to guarantee fully reproducible training results across execution sessions. |
| Standardised Quantitative Evaluation Metrics | ✅ Regression suite: MSE, RMSE, R² Score; Classification suite: Global Accuracy, Class-wise Precision, Recall, F1-Score. All metrics paired with plain-language interpretive annotations. |
| Dynamic Model Diagnostics Visualisations | ✅ Classification output: Normalised confusion matrix heatmap labelled with target variable metadata; Regression output: Actual vs. Predicted value scatter plot for residual analysis. |

---
## ✨ Core Platform Capabilities
### 🔐 Enterprise-Grade Data Privacy & Secure Ingestion
- **Zero Cloud Data Egress Architecture**: All dataset parsing, feature engineering, model training, and visualisation rendering executes locally on the end-user’s hardware. No raw or derived data payloads are transmitted to external cloud APIs or remote servers.
- **Configurable CSV Header Inference**: Automated schema detection with manual override controls for non-standard CSV formatting.
- **Low-Latency Dataset Sampling Preview**: Instant rendering of top-five dataset records immediately post-upload for rapid data quality validation.
- **Robust Input Sanitisation Layer**: Strict file extension and MIME-type filtering with granular error messaging for invalid, corrupted, or unsupported input payloads.

### 🧠 Automated ML Pipeline Orchestration
- **Statistical Task Inference Engine**: Unsupervised type analysis to auto-distinguish regression and classification modelling tasks without manual user input.
- **Context-Aware Model Selector UI**: Model library dynamically filters to display only estimators compatible with the detected supervised learning task; all baseline algorithms pre-configured with sensible default hyperparameters for rapid prototyping.
- **Flexible Target Variable Selection**: Default mapping to last dataset column with interactive dropdown for custom target feature assignment.

### 📊 Standardised Model Training & Performance Analytics
- **Deterministic Train/Test Partitioning**: Fixed random state ensures identical dataset splits across repeated training runs for reproducible benchmarking.
- **Comprehensive Univariate Target Statistics Panel**: Complete quantile and distribution metrics to enable preliminary target variable quality assessment prior to training.
- **Industry-Standard Evaluation Metric Suites**: Task-aligned quantitative scoring with embedded plain-text definitions to reduce interpretive friction for non-specialist users.
- **Contextualised Diagnostic Visualisations**: Labelled, publication-ready plots for residual and classification error analysis, dynamically titled with active target feature metadata.
- **Dataset Partition Metadata Dashboard**: Real-time display of total record count, training sample volume, test sample volume, and proportional split percentages for audit transparency.

### 🔎 Model Explainability & Algorithmic Governance
- **Multi-Source Feature Importance Ranking**: Hybrid importance calculation combining mutual information statistical scoring and Random Forest feature weight attribution, aggregated and grouped by original input column identifiers for intuitive interpretability.
- **Pre-Execution Data Consistency Guardrails**: Contextual warning notifications alert users to configuration mismatches (e.g., continuous target variable assigned to classification task) to prevent invalid model training workflows.
- **Human-Centric Metric Labelling**: Every quantitative metric includes plain-language guidance (e.g., "MSE: Lower numerical values indicate superior predictive performance") to standardise result interpretation across skill levels.

### 🎨 Production-Grade User Experience & Interface Design
- **Mobile-First Responsive Web UI**: Compact, modular component layout optimised for desktop, laptop, and tablet viewing resolutions.
- **Automated Viewport Scrolling Logic**: Post-computation auto-scroll functionality navigates the UI to newly generated statistical or training result panels to minimise manual user navigation overhead.
- **Modular Training Control Card**: Dedicated, isolated UI component housing training configuration parameters and a single-click execution trigger for streamlined model training initiation.

---
## 🛠 Full Technology Stack
| Architectural Layer | Production Technology Suite |
| :--- | :--- |
| Application Backend API | Python 3.10+, FastAPI 0.115+, Uvicorn ASGI Production Server |
| Data Processing & Machine Learning Core | Pandas, NumPy, Scikit-learn v1.5+ |
| Static Visualisation Rendering | Matplotlib (server-side plot generation, base64 payload delivery to frontend) |
| Client-Side Frontend Interface | HTML5 Semantic Markup, CSS3 Custom Properties, Vanilla ES6+ JavaScript (zero external frontend framework dependencies) |
| Deployment Targets | Static frontend asset hosting via GitHub Pages; backend restricted to local workstation execution only |

---
# 🚀 Installation & Environment Provisioning
This section formalises a reproducible, step-by-step environment setup workflow for Windows, macOS, and Linux operating systems, including pre-flight validation, repository acquisition, dependency provisioning, and backend service initialisation. All commands follow cross-platform best practices with platform-specific callouts where applicable.

## 1. Pre-Flight Prerequisite Validation
Complete the below environment audit before repository deployment to eliminate runtime dependency failures. All listed tooling is mandatory for full platform functionality.

| Prerequisite Component | Formal Description | Validation Command | Criticality Rationale |
| :--- | :--- | :--- | :--- |
| Python 3.10 or Newer Interpreter | Core runtime environment powering the FastAPI backend, data parsing, and machine learning computation layers. | Terminal / Command Prompt:<br>`python --version`<br>macOS/Linux fallback: `python3 --version` | The backend and ML core are natively implemented in Python; incompatible minor/major versions introduce breaking API and library compatibility errors. |
| Python Package Installer (pip) | Official Python package management utility bundled with standard Python 3.10+ distributions, used to resolve and install all third-party dependency libraries. | Terminal / Command Prompt:<br>`pip --version`<br>macOS/Linux fallback: `pip3 --version` | Required to provision the complete ML and API dependency stack; no alternative package managers are officially supported for this project. |
| Standards-Compliant Modern Web Browser | Rendering engine for the static frontend web interface; supports ES6+ JavaScript, modern CSS, and base64 image payload ingestion for visualisation rendering. | N/A (Manual version check via browser "About" menu) | Legacy browsers lack required JavaScript and DOM APIs to execute the full frontend interactive workflow. Recommended releases: Google Chrome, Microsoft Edge, Mozilla Firefox, Apple Safari (latest stable channel builds). |
| Git Version Control System (Optional) | Distributed source control client to clone the remote GitHub repository source code. | Terminal / Command Prompt:<br>`git --version` | Only required for repository cloning workflows. If Git is unavailable, users may download the project source as a compressed ZIP archive directly from the repository GitHub page. |

## 2. Repository Source Code Acquisition
Two officially supported deployment pathways are provided for source code retrieval; the Git clone method is recommended for future project update compatibility.

### Option A: Git Repository Clone (Recommended)
1. Launch your native system terminal (Terminal on macOS/Linux, PowerShell / Command Prompt on Windows).
2. Navigate to a target working directory where the project source will be stored locally (example directory command provided below).
3. Execute the repository clone command to pull the complete source tree from GitHub.
4. Enter the project root directory post-clone completion.

```bash
# Navigate to your preferred project storage directory (example for cross-platform consistency)
cd ~/Projects
# Clone the public source repository
git clone https://github.com/Rishad45-dot/automl-lite.git
# Enter the project root working directory
cd automl-lite
```

### Option B: ZIP Archive Manual Download (Git-Free Workflow)
1. Navigate to the project GitHub repository homepage in your web browser.
2. Locate the **Code** dropdown button in the upper-right repository navigation panel.
3. Select the **Download ZIP** option to initiate a compressed source archive download.
4. Extract the full archive contents to a dedicated local working directory of your choice.
5. Open your system terminal and change directory to the extracted project root folder prior to proceeding with dependency installation.

## 3. Isolated Python Virtual Environment Provisioning (Mandatory Best Practice)
To prevent global Python package version conflicts and ensure fully reproducible dependency resolution across environments, a dedicated isolated virtual environment is required. Platform-specific activation syntax is documented below.

### Step 3.1: Initialise Virtual Environment
Execute this single command within the project root directory to generate a self-contained Python environment folder named `venv`:
```bash
# Cross-platform virtual environment initialisation
python -m venv venv
# macOS / Linux fallback if python alias maps to Python 2
python3 -m venv venv
```

### Step 3.2: Activate the Isolated Virtual Environment
Run the platform-specific activation command matching your operating system; successful activation will prefix your terminal prompt with `(venv)` to confirm isolation.
```bash
# Windows (Command Prompt / CMD.exe)
venv\Scripts\activate.bat

# Windows (PowerShell)
.\venv\Scripts\Activate.ps1

# macOS / Linux (Bash / Zsh Terminal)
source venv/bin/activate
```

> **Critical PowerShell Note for Windows Users**: If script execution policies block virtual environment activation, execute this administrative PowerShell command once to permit local script execution:
> ```powershell
> Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```
> Select `Y` to confirm policy modification when prompted.

## 4. Third-Party Dependency Installation
With the virtual environment active, install the complete pinned dependency stack via the project’s `requirements.txt` manifest file to lock consistent library versions.
```bash
# Standard dependency install command (all platforms)
pip install -r requirements.txt
# macOS / Linux fallback alias
pip3 install -r requirements.txt
```

### Post-Install Validation Check
Verify successful dependency provisioning by executing the following import test command; no module import errors confirm a complete environment setup:
```bash
python -c "import fastapi, uvicorn, pandas, numpy, sklearn, matplotlib; print('All core dependencies installed successfully')"
```

## 5. Backend API Service Initialisation
Launch the FastAPI ASGI backend server using Uvicorn within the active virtual environment. Two execution modes are provided for development and standard runtime use cases.

### Standard Production-Like Runtime Mode
Suitable for end-user model training workflows; disables auto-reload to optimise compute performance:
```bash
uvicorn main:app --host 127.0.0.1 --port 8000
```

### Development Debug Mode (For Code Modification Only)
Enables live server auto-reload on source file edits; intended exclusively for platform development and customisation:
```bash
uvicorn main:app --host 127.0.0.1 --port 8000 --reload
```

### Post-Startup Validation
Upon successful backend initialisation, the terminal will output confirmation logging with the local service endpoint address:
`http://127.0.0.1:8000`
- Access interactive API documentation via auto-generated Swagger UI: `http://127.0.0.1:8000/docs`
- The static frontend GitHub Pages deployment will communicate with this local backend endpoint for all dataset and modelling operations.

## 6. Post-Runtime Environment Deactivation
When all modelling workflows are complete and you wish to exit the isolated virtual environment, run the single deactivation command in the terminal:
```bash
deactivate
```

## Troubleshooting Common Installation Failures
1. **Python Version Mismatch Errors**: Download and install Python 3.10+ from the official Python Software Foundation website; ensure the new interpreter is added to your system PATH environment variable.
2. **pip Command Not Found**: Re-run the Python installer and enable the "Add Python to PATH" checkbox during installation, or use the Python interpreter module syntax `python -m pip install [package]`.
3. **Matplotlib Render Backend Errors (Linux/macOS)**: Install system-level graphical rendering dependencies via native package managers (apt, brew) to resolve missing GUI backend libraries.
4. **Port 8000 Already In Use**: Modify the Uvicorn launch command to utilise an alternative port number (example `--port 8001`).

---
## End-to-End User Workflow Guide
1. Start the FastAPI backend server following the installation steps above.
2. Navigate to the live GitHub Pages frontend URL in a modern web browser.
3. Upload a valid CSV file via drag-and-drop or file selection button.
4. Review auto-generated data preview and descriptive statistics for data quality checks.
5. Adjust header toggle, target column, and supervised task type as needed.
6. Select your preferred ML algorithm from the filtered model list.
7. Click the training button to initiate model fitting on the 80/20 train-test split.
8. Review evaluation metrics, diagnostic visualisations, and feature importance rankings.
9. Repeat with alternative models to compare predictive performance.

## Standardized Project Directory Structure
```
automl-lite/
├── main.py                 # FastAPI backend application entrypoint
├── requirements.txt       # Pinned Python dependency manifest
├── static/                 # Frontend static assets
│   ├── index.html
│   ├── style.css
│   └── script.js
├── assets/                 # Generated plots, local dataset cache
├── LICENSE                 # MIT open-source license file
└── README.md               # Project documentation
```

## Responsible AI Governance Framework
This platform embeds four core Responsible AI pillars into its end-to-end workflow:
1. **Privacy-by-Design**: All data processing remains local; zero external data transmission.
2. **Algorithmic Transparency**: Full visibility over train-test split logic, model hyperparameters, and scoring formula definitions.
3. **Model Explainability**: Feature importance visualisations to quantify predictor impact on target outputs.
4. **Human-In-The-Loop Oversight**: Manual overrides for auto-detected schema, task type, and guardrail warnings for invalid modelling configurations.

## System Limitations & Product Roadmap
### Current Platform Limitations
- Restricted to tabular CSV structured data only; unstructured text/image inputs unsupported.
- Baseline classical ML estimators exclusively; deep learning neural network integration not implemented.
- No persistent model serialisation/export functionality for offline inference deployment.
- Limited hyperparameter tuning controls; fixed default estimator configurations.
- No native handling of missing value imputation or advanced categorical encoding.

### Future Development Roadmap
1. Hyperparameter grid/random search optimisation module
2. Trained model weight export (`.pkl`) and offline inference endpoint
3. Automated missing value imputation and categorical encoding pipelines
4. Extended interpretability tooling (SHAP value visualisations)
5. Lightweight dark mode UI theme toggle
6. Support for larger dataset chunked streaming processing
7. Export full training report as PDF/CSV

## Project Deliverable Inventory
All artefacts included within the repository source tree:
- FastAPI backend source (`main.py`)
- Static frontend HTML/CSS/JS assets
- Dependency manifest (`requirements.txt`)
- Complete project documentation (`README.md`)
- MIT open-source `LICENSE` file
- Local asset directories for plots and temporary data storage

## Software License
This open-source project is distributed under the MIT License — permissive commercial and non-commercial use permitted with standard copyright attribution requirements. Full license text available within the root-level `LICENSE` file of the repository.

## Attributions & Acknowledgements
Recognition for the maintainers and contributors of all open-source libraries powering AutoML-Lite:
- FastAPI & Uvicorn for high-performance local API hosting
- Pandas & NumPy for tabular data manipulation
- Scikit-learn for classical supervised machine learning pipelines
- Matplotlib for model diagnostic visualisation
- Web standards communities for HTML/CSS/ES6 frontend tooling
```

=======
cd automl-lite
>>>>>>> 6a6eda38ee27f5238359f10a9d522343c46476ad
