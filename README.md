# 🔌 LPDG Innovation Hub - Gateway Visit Prioritization 2026

An advanced machine learning and telemetry-driven analytics dashboard designed to optimize IoT gateway field visits, minimize operational costs, and maximize network reliability.

---

## 🌐 Live Demo

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-streamlit-app-url.streamlit.app)

---

## 📋 Project Overview

Managing IoT gateway health efficiently is crucial to reducing operational overhead. Under the challenge cost framework where false alarms cost **€380** and missed faults cost **€600**, this project implements a smart risk-scoring and prioritization pipeline.

Using 28-day historical telemetry trends (`offline_duration_sec`, `disconnection_cnt`, `reboot_cnt`), the machine learning model ranks the top **15 gateways per week** for field interventions, successfully lowering proxy operational costs down to **€270,600** (saving **€58,800** compared to the baseline).

---

## ✨ Features

* **Telemetry-Driven Risk Scoring (`ml_model.py`):** Automatically calculates rolling telemetry features and prioritizes high-risk gateways per week.
* **Interactive Streamlit Web App (`app.py`):** A professional, dark-themed dashboard featuring executive summaries, operational cost metrics, interactive charts, and a gateway ID search explorer.
* **Rigorous Validation (`validate_submission.py`):** Ensures all prediction outputs conform strictly to the required submission schema and constraints.

---

## 🛠️ Prerequisites

* **Python 3.10+** (Required)
* **pip** (Python package manager)
* **Git** (For cloning the repository)

---

## 📁 Project Structure

```text
LPDG-Innovation-Challenge/
├── data/                  # Input challenge dataset files
├── ml_model.py            # Machine learning & scoring script
├── validate_submission.py # Schema validation script
├── app.py                 # Streamlit web application
├── predictions.csv        # Generated weekly predictions output
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation

📦 Installation & Setup
Clone the repository:

git clone https://github.com/PSaiSudha/LPDG-Innovation-Challenge.git
cd LPDG-Innovation-Challenge

Install dependencies:

pip install -r requirements.txt

🚀 Usage
Step 1: Generate Predictions
Run the machine learning script to process telemetry data and generate weekly prioritized gateway visits:

python ml_model.py
(This generates the predictions.csv file)

Step 2: Validate Submission File
Verify that your predictions adhere to all structural and constraint rules:

python validate_submission.py predictions.csv

Step 3: Launch the Web Dashboard
Explore the executive metrics and interactive visualizations locally:

python -m streamlit run app.py

📊 Results & Financial Impact
- Baseline Cost (Part 1): €329,400
- Optimized ML Cost (Part 2): €270,600
- Total Estimated Savings: €58,800
- Weekly Visit Constraint: Exactly 15 gateways per week across evaluation periods.

💡 Key Insights
- Proactive Intervention: Prioritizing unstable nodes based on historical reboots and disconnection counters prevents cascading network failures.
- Cost-Aware Optimization: Direct alignment with financial penalties ensures maximum savings on field technician dispatches.
- Reproducible Pipeline: Clean automation scripts from raw data parsing to final evaluation submission.

🤝 Contributing
This is an innovation challenge solution project for gateway maintenance optimization. Feel free to extend it with alternative ranking metrics, advanced classification algorithms, or automated alerting hooks!
