# ➕ LPDG Innovation Hub – Gateway Visit Prioritization 2026

An advanced **machine learning and telemetry-driven analytics dashboard** designed to optimize IoT gateway field visits, minimize operational costs, and maximize network reliability.

---

## 🌐 Live Demo

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-streamlit-app-url.streamlit.app)

---

## 📋 Project Overview

Managing IoT gateway health efficiently is crucial for reducing operational overhead and maintaining network reliability.

Under the challenge cost framework:

* **False Alarm Cost:** €380
* **Missed Fault Cost:** €600

This project implements a **machine learning-based risk scoring and prioritization pipeline** that analyzes historical IoT gateway telemetry and identifies gateways that should be prioritized for field intervention.

The model uses **28-day historical telemetry trends**, including:

* `offline_duration_sec`
* `disconnection_cnt`
* `reboot_cnt`

Based on these telemetry patterns, gateways are assigned risk scores and ranked for weekly field visits.

The system prioritizes the **top 15 gateways per week**, helping reduce unnecessary operational costs while focusing technician visits on gateways with higher predicted risk.

### 🎯 Key Result

The optimized approach achieved a proxy operational cost of:

**€270,600**

compared with the baseline cost of:

**€329,400**

### 💰 Estimated Savings

**€58,800**

---

## ✨ Features

### 1. Telemetry-Driven Risk Scoring

**File:** `ml_model.py`

The machine learning pipeline:

* Processes historical gateway telemetry.
* Calculates rolling 28-day features.
* Analyzes gateway stability and failure-related patterns.
* Generates risk scores.
* Ranks gateways based on predicted risk.
* Selects the top 15 gateways for weekly field intervention.
* Generates the final `predictions.csv` file.

---

### 2. Interactive Streamlit Dashboard

**File:** `app.py`

The project includes an interactive web dashboard built using **Streamlit**.

The dashboard provides:

* Executive-level project summary.
* Operational cost metrics.
* Baseline vs optimized cost comparison.
* Estimated savings.
* Gateway risk analysis.
* Interactive charts.
* Weekly gateway prioritization.
* Gateway ID search and exploration.
* Telemetry-based insights.

---

### 3. Submission Validation

**File:** `validate_submission.py`

The validation script verifies that the generated prediction file follows the required challenge format.

It checks:

* Required columns.
* Data structure.
* Prediction format.
* Weekly visit constraints.
* Required number of gateways.
* Submission consistency.

---

## 🛠️ Technologies Used

* **Python 3.10+**
* **Pandas**
* **NumPy**
* **Scikit-learn**
* **Streamlit**
* **Matplotlib / Seaborn**
* **Git & GitHub**
* **Machine Learning**
* **IoT Telemetry Analytics**
* **Data Analysis**
* **Risk Scoring**

---

## 📁 Project Structure

```text
LPDG-Innovation-Challenge/
│
├── data/
│   └── # Input challenge dataset files
│
├── ml_model.py
│   └── Machine learning and gateway risk-scoring pipeline
│
├── validate_submission.py
│   └── Prediction schema and constraint validation
│
├── app.py
│   └── Streamlit analytics dashboard
│
├── predictions.csv
│   └── Generated weekly gateway prioritization results
│
├── requirements.txt
│   └── Python dependencies
│
└── README.md
    └── Project documentation
```

---

## 📦 Prerequisites

Before running the project, make sure the following are installed:

* **Python 3.10 or higher**
* **pip**
* **Git**

You can verify Python installation using:

```bash
python --version
```

And verify pip using:

```bash
pip --version
```

---

## 🚀 Installation & Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/PSaiSudha/LPDG-Innovation-Challenge.git
```

Move into the project directory:

```bash
cd LPDG-Innovation-Challenge
```

---

### Step 2: Install Dependencies

Install all required Python packages:

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

### Step 1: Generate Predictions

Run the machine learning pipeline:

```bash
python ml_model.py
```

This processes the telemetry data and generates:

```text
predictions.csv
```

The generated file contains the weekly prioritized gateways.

---

### Step 2: Validate the Prediction File

Run the validation script:

```bash
python validate_submission.py predictions.csv
```

This verifies that the prediction file follows the required challenge schema and constraints.

---

### Step 3: Launch the Streamlit Dashboard

Start the dashboard locally using:

```bash
python -m streamlit run app.py
```

After running the command, open the displayed local URL in your browser.

---

## 📊 Results & Financial Impact

| Metric                  |       Value |
| ----------------------- | ----------: |
| Baseline Cost           |    €329,400 |
| Optimized ML Cost       |    €270,600 |
| Estimated Savings       |     €58,800 |
| Weekly Visit Constraint | 15 gateways |

### Cost Reduction

The optimized ML-based prioritization reduces the proxy operational cost from:

**€329,400 → €270,600**

representing an estimated saving of:

**€58,800**

---

## 🧠 How the System Works

The overall workflow can be summarized as:

```text
Historical Gateway Telemetry
            ↓
      Data Processing
            ↓
   28-Day Rolling Features
            ↓
      Risk Scoring
            ↓
    Gateway Ranking
            ↓
 Select Top 15 Gateways / Week
            ↓
      predictions.csv
            ↓
   Validation & Dashboard
```

---

## 📡 Telemetry Features

The system primarily uses historical gateway telemetry signals such as:

### `offline_duration_sec`

Measures the amount of time a gateway remains offline.

Higher or increasing offline duration can indicate gateway instability.

### `disconnection_cnt`

Represents the number of gateway disconnection events.

Repeated disconnections may indicate an unstable gateway or connectivity problem.

### `reboot_cnt`

Represents the number of gateway reboot events.

Frequent reboots can be an indicator of gateway instability.

---

## 💡 Key Insights

### 🔹 Proactive Intervention

Historical telemetry patterns can be used to identify unstable gateways before they result in larger network issues.

### 🔹 Cost-Aware Prioritization

The prioritization strategy considers the challenge's different costs for false alarms and missed faults.

* False Alarm: **€380**
* Missed Fault: **€600**

This makes gateway prioritization a cost-sensitive decision rather than simply selecting gateways based on a single telemetry metric.

### 🔹 Weekly Prioritization

The system selects exactly **15 gateways per week** during the evaluation period, following the challenge constraint.

### 🔹 Reproducible Pipeline

The project provides a reproducible workflow:

```text
Raw Data
   ↓
Feature Engineering
   ↓
Risk Scoring
   ↓
Gateway Ranking
   ↓
Prediction Generation
   ↓
Validation
   ↓
Dashboard
```

---

## 📈 Dashboard

The Streamlit dashboard provides an interactive way to explore the model's results.

Users can view:

* Overall operational cost.
* Estimated savings.
* Weekly gateway selections.
* Gateway risk information.
* Telemetry trends.
* Gateway-specific information.
* Interactive visualizations.

---

## 🔍 Gateway Explorer

The dashboard includes a gateway search feature that allows users to search for a specific gateway ID and inspect its available telemetry and prioritization information.

This helps field and operations teams understand why a particular gateway may have been prioritized.

---

## 🔐 Validation

Before using the generated predictions as the final challenge submission, run:

```bash
python validate_submission.py predictions.csv
```

The validation step helps ensure that the generated output satisfies the required structural and weekly constraints.

---

## 📌 Challenge Constraints

The solution follows the key challenge requirements:

* Historical telemetry is used for gateway risk analysis.
* A 28-day historical window is considered for feature engineering.
* Gateways are ranked based on risk.
* Exactly **15 gateways are selected per week**.
* The generated predictions follow the required submission structure.
* The prediction file is validated before submission.

---

## 🤝 Contributing

This project was developed as a solution for the **LPDG Innovation Challenge 2026**.

The project can be further extended with:

* Advanced classification algorithms.
* Gradient boosting models.
* Time-series forecasting.
* Anomaly detection.
* Gateway failure probability estimation.
* Automated alerting.
* Real-time telemetry processing.
* Technician route optimization.
* Cost-sensitive machine learning.
* Automated monitoring and reporting.

---

## 👩‍💻 Author

**PSaiSudha**

GitHub:
https://github.com/PSaiSudha

---

## ⭐ Project Summary

**LPDG Innovation Hub** combines machine learning, IoT telemetry analytics, and an interactive Streamlit dashboard to prioritize IoT gateway field visits.

By analyzing historical gateway behavior and ranking gateways according to their risk, the system provides a data-driven approach to field maintenance prioritization while considering operational costs.

**Baseline Cost:** €329,400
**Optimized Cost:** €270,600
**Estimated Savings:** €58,800
**Weekly Visits:** 15 gateways
