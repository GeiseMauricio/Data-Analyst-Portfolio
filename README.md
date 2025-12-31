# 💳 Credit Card Fraud Analysis

## 📌 Project Overview

This project presents an end-to-end data analysis pipeline focused on detecting fraudulent credit card transactions.  
The objective is to explore the data, understand fraud patterns, deal with extreme class imbalance, and prepare the dataset for modeling, following industry-standard best practices.

The project is designed to be **reproducible, well-structured, and portfolio-ready**, showcasing skills expected from a **Data Analyst / Junior Data Scientist**.

---

## 🎯 Objectives

- Explore and understand credit card transaction data  
- Perform exploratory data analysis (EDA) focused on fraud detection  
- Analyze and visualize class imbalance  
- Prepare clean and processed datasets for modeling  
- Build a clear and reproducible analysis pipeline  

---
## 📂 Project Structure


credit-card-fraud-analysis/
│
├── data/
│   ├── raw/            # Raw data (not included due to size limits)
│   └── processed/      # Cleaned and processed datasets
│
├── notebooks/          # Jupyter notebooks with the analysis pipeline
│   ├── 01_eda_fraud_analysis.ipynb
│   └── 02_modeling_fraud_risk_exploration.ipynb
│
├── outputs/            # Figures, charts, and analysis results
├── config/             # Configuration files (if applicable)
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
└── .gitignore


---
## 📊 Dataset

Source: Kaggle – Credit Card Fraud Detection Dataset

Download:
https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

Dataset Description

Transactions made by European cardholders

Highly imbalanced dataset (fraud ≈ 0.17%)

Features anonymized using PCA

Target Variable

Class = 1 → Fraud

Class = 0 → Legitimate transaction

---

## ⚠️ Raw Data Policy

The raw dataset file (creditcard.csv) is not included in this repository due to GitHub file size limits.

To run the project locally:

Download the dataset from Kaggle

Place the file in the following path:
data/raw/creditcard.csv

---

## 🔍 Analysis Highlights

Overview of dataset structure and summary statistics

Visualization of extreme class imbalance

Distribution analysis of transaction amounts

Comparison between fraudulent and non-fraudulent transactions

Data preprocessing and feature scaling

Clean, modular, and well-documented notebooks

All visualizations and intermediate results saved in the outputs/ directory

---

## 🧪 Tools & Technologies

Python

Pandas & NumPy – data manipulation

Matplotlib & Seaborn – data visualization

Scikit-learn – preprocessing utilities

Jupyter Notebook – analysis environment

Git & GitHub – version control

---

## ▶️ How to Run
1. Clone the repository
git clone https://github.com/GeiseMauricio/Data-Analyst-Portfolio.git

2. Navigate to the project directory
cd credit-card-fraud-analysis

3. Install dependencies
pip install -r requirements.txt

4. Download the dataset

Place creditcard.csv in:

data/raw/creditcard.csv

5. Open the notebooks
jupyter notebook notebooks/01_eda_fraud_analysis.ipynb
jupyter notebook notebooks/02_modeling_fraud_risk_exploration.ipynb

---

## 📈 Results

This project delivers:

Clear visual insights into fraud patterns

Processed datasets ready for modeling

A reproducible and well-documented analysis pipeline

The focus is on data understanding and preparation, which are critical steps in real-world fraud detection projects.

---

## 🚀 Next Steps

Implement and compare classification models

Apply resampling techniques (SMOTE, undersampling)

Evaluate models using precision-recall metrics

Create a dashboard to communicate results

Translate findings into business insights

---

## 👩‍💻 Author

Geisiana Maurício
Data Analyst | Data Analytics & Data Science

🔗 GitHub: https://github.com/GeiseMauricio