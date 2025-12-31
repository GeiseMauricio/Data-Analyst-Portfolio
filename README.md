⚙️ Methodology

1. Data Loading

CSV ingestion from the Kaggle Credit Card Fraud dataset

Initial data inspection (shape, data types, missing values)

2. Data Understanding & Exploration (EDA)

Exploratory analysis focused on fraudulent vs. non-fraudulent transactions

Analysis of extreme class imbalance (fraud ≈ 0.17%)

Distribution analysis of transaction amounts

Comparison between fraud and legitimate transactions

Identification of relevant patterns and anomalies

3. Data Preparation

Feature scaling of the Amount variable

Dataset organization and cleaning

Preparation of processed data for future modeling steps

⚠️ Note: Features V1–V28 are already anonymized using PCA by the data provider. No additional dimensionality reduction was applied.

📊 Key Insights

Strong class imbalance, requiring special treatment in modeling stages

Fraudulent transactions tend to present different amount distributions compared to legitimate ones

PCA-transformed features capture meaningful variance despite anonymization

📈 Business Perspective

In credit card fraud detection, understanding the data is a critical first step.
This analysis focuses on data quality, imbalance awareness, and behavioral patterns, which directly support better decision-making and model design in later stages.

🚀 Technologies Used

Python

Pandas & NumPy — data manipulation

Matplotlib & Seaborn — data visualization

Scikit-learn — preprocessing utilities

Jupyter Notebook

Git & GitHub — version control

🚧 Next Steps

Build baseline classification models

Apply resampling techniques (e.g., SMOTE, undersampling)

Evaluate models using precision, recall, and PR-AUC

Threshold tuning focused on fraud recall

Develop a dashboard layer for result communication

📌 Author

Geisiana Maurício
Data Analyst | Statistical Analysis | Fraud Detection