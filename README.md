# Customer Churn Prediction using Machine Learning

## Project Overview

Customer churn is a major challenge for telecom companies because losing customers directly impacts revenue. This project builds a machine learning model to predict whether a customer will churn based on demographic, service usage, and billing information.

The goal is to help companies identify customers who are likely to leave so they can take preventive actions.

---

## Dataset

The dataset contains telecom customer information including:

* Customer demographics
* Services subscribed
* Billing information
* Contract type
* Payment method
* Churn status (target variable)

After preprocessing the dataset contains **7032 rows and 24 features**.

---

## Machine Learning Workflow

1. Data Cleaning
2. Handling Missing Values
3. Feature Encoding using One-Hot Encoding
4. Feature Scaling using StandardScaler
5. Train-Test Split
6. Model Training
7. Model Evaluation

---

## Models Used

* Logistic Regression
* Decision Tree
* Random Forest

Logistic Regression performed best for this dataset.

---

## Model Evaluation

Confusion Matrix:

[[913 105]
[194 195]]

Performance Metrics:

* Accuracy: **78%**
* Precision: **65%**
* Recall: **50%**
* F1 Score: **0.56**

---

## Visualizations

### Customer Churn Distribution

![Churn Distribution](images/churn_distribution.png)

### Monthly Charges vs Churn

![Monthly Charges vs Churn](images/monthly_charges_churn.png)

### Tenure vs Churn

![Tenure vs Churn](images/tenure_churn.png)


## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Jupyter Notebook

---

## Project Structure

customer-churn-prediction
│
├── data
│   └── churn.csv
│
├── notebook
│   └── churn_analysis.ipynb
│
├── src
│   └── model.py
│
├── requirements.txt
└── README.md

---

## Future Improvements

* Improve recall using advanced models
* Hyperparameter tuning
* Apply SMOTE for class imbalance
* Try Gradient Boosting / XGBoost

---

## Author

Machine Learning project created as part of AI/ML learning journey.
