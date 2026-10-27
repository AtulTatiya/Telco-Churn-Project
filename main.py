import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# 1. Load the data
df = pd.read_csv("data/Telco-Customer-Churn.csv")

# 2. Data Cleaning
# Handle blank spaces in 'TotalCharges' by converting to numeric and dropping NaNs
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df.dropna(subset=['TotalCharges'], inplace=True) 

# 3. Feature Engineering
# Identify premium users paying > $70/month
df['is_premium'] = df['MonthlyCharges'].apply(lambda x: 1 if x > 70.0 else 0)
# Calculate user's charge vs the average for their contract type
df['avg_contract_charge'] = df.groupby('Contract')['MonthlyCharges'].transform('mean')
df['charge_difference'] = df['MonthlyCharges'] - df['avg_contract_charge']

# Mock the AI sentiment score based on churn status for simulation purposes
np.random.seed(42)
df['sentiment_score'] = np.where(
    df['Churn'] == 'Yes', 
    np.random.uniform(-1.0, 0.2, len(df)), 
    np.random.uniform(-0.2, 1.0, len(df))
)

# 4. Prepare for Modeling
df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})
y = df['Churn']
X = df.drop(columns=['Churn', 'customerID'])

# Convert categorical variables into dummy/indicator variables
X_encoded = pd.get_dummies(X, drop_first=True)

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, stratify=y, random_state=42)

# Train the Random Forest Model with balanced class weights
model = RandomForestClassifier(n_estimators=100, class_weight='balanced', random_state=42)
model.fit(X_train, y_train)

# Output Evaluation
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))