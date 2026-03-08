# AI PCB Test Predictor

![Python](https://img.shields.io/badge/Python-3.10%2B-blue) ![License](https://img.shields.io/badge/License-MIT-green) ![GitHub stars](https://img.shields.io/github/stars/YourUsername/pcb-ai-test-system?style=social)

Ever wondered if we could predict whether a PCB will pass or fail **before testing it physically**? That’s exactly what this project does! Using **synthetic test data** and **machine learning**, this project predicts PCB test outcomes and gives you a clear picture of potential failures — all in Python.

---

🚀 Features

-- Simulates PCB test measurements (voltage, current, temperature, time)
-- Trains a Random Forest classifier to predict PASS/FAIL
-- CLI script for new PCB predictions
-- Optional Streamlit dashboard for interactive visualization

📂 Project Structure

pcb-ai-test-system/
├── data/               # Synthetic PCB test data
├── src/                # Scripts: data generation, training, prediction
├── notebooks/          # Analysis notebooks
├── dashboard.py        # Streamlit dashboard
├── requirements.txt    # Python dependencies
└── README.md
