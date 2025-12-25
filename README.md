
---

## ⚙️ Methodology

### 1. Data Loading
- CSV ingestion
- Basic validation and structure inspection

### 2. Handling Class Imbalance
- SMOTE (Synthetic Minority Over-sampling Technique)
- Ensures balanced class distribution for training

### 3. Modeling
- Random Forest Classifier
- Robust to non-linear patterns and noisy data

### 4. Evaluation
- Recall prioritized over accuracy
- Threshold tuning to achieve recall > 95%
- ROC Curve and AUC

### 5. Explainability
- SHAP values for global and local interpretability
- Transparency for financial decision-making

---

## 📊 Key Results
- ROC-AUC: High discriminative performance
- Recall > 95% after threshold optimization
- Clear feature importance and explainability via SHAP

---

## 📈 Business Perspective
In fraud detection, minimizing false negatives is critical.
This project prioritizes recall to reduce financial losses, accepting a higher number of false positives as a trade-off.

---

## 🚀 Technologies Used
- Python
- Pandas, NumPy
- Scikit-learn
- Imbalanced-learn
- SHAP
- Matplotlib / Seaborn
- Power BI (dashboard layer)

---

## 📌 Author
**Geisiana Maurício**  
Data Analyst | Statistical Modeling | Fraud Detection
