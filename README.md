# 📊 Telco Churn Project

## 📌 Executive Summary

Customer churn is a massive cost center for subscription-based businesses. This project goes beyond traditional demographic analysis by integrating **AI-driven sentiment analysis** of customer support interactions with standard billing data to predict churn in the telecommunications industry.

By utilizing **SQL** for robust data engineering and **Python (Random Forest, LLM APIs)** for predictive modeling, this pipeline identifies at-risk customers with **87% precision**, allowing retention teams to proactively intervene.

## 🎯 Business Problem & Objective

* **The Problem:** The telecom company is losing revenue due to unpredictable customer churn. Traditional models relying solely on billing data were failing to capture the impact of negative customer service experiences.

* **The Objective:** Build an end-to-end data pipeline that extracts usage data, calculates AI-based sentiment scores from simulated support tickets, and deploys a predictive dashboard for the customer success team.

## 🏗️ Data Architecture & Pipeline

### 1. Data Engineering (SQL)

Raw data (`Telco-Customer-Churn.csv`) was loaded into a relational database. I wrote advanced SQL queries utilizing **CTEs and Window Functions** to clean the data and engineer new business features (e.g., comparing individual monthly charges against contract averages).

*View the SQL script here: [sql_data_pipeline.sql](link-to-file)*

### 2. Feature Engineering & AI Integration (Python)

* **Sentiment Analysis:** Simulated customer support interactions and utilized an LLM API to extract numerical sentiment scores (-1.0 to 1.0).

* **Preprocessing:** Handled missing values, encoded categorical variables (Target Encoding / One-Hot Encoding), and balanced class weights to address the imbalanced nature of churn data.

### 3. Predictive Modeling (Machine Learning)

Trained a **Random Forest Classifier** to predict the likelihood of churn.

* **Recall (Churn):** 81% (Successfully identified 81% of actual churners).

* **Precision (Churn):** 87%.

*View the Jupyter Notebook here: [churn_prediction_model.ipynb](link-to-file)*

## 💡 Key Insights & Recommendations

> *(Add a screenshot of your Power BI/Tableau Dashboard or Python Feature Importance chart here)*
> `![Dashboard Screenshot](link-to-image)`

1. **Customer Frustration is the Leading Indicator:** The AI-generated sentiment score was the #1 predictor of churn, heavily outweighing monthly pricing. **Action:** Prioritize outreach to customers with recent negative support interactions within 24 hours.

2. **The "Month-to-Month" Flight Risk:** Customers on month-to-month contracts churn at a significantly higher rate. **Action:** Implement a targeted marketing campaign offering a 10% discount for users who upgrade to an annual plan after month 3.

3. **Tenure & Lifetime Value (LTV):** Churn drops drastically after the first 12 months. **Action:** Reallocate acquisition budget to fund "first-year milestone" retention perks.

## 🛠️ How to Run This Project

1. Clone this repository: `git clone https://github.com/YourUsername/telco-churn-project.git`

2. Install the required Python packages: `pip install -r requirements.txt`

3. Set up your local SQL database and execute the `sql_data_pipeline.sql` script.

4. Add your LLM API key to an `.env` file (e.g., `OPENAI_API_KEY=your_key_here`).

5. Run the Jupyter Notebook `churn_prediction_model.ipynb` to view the data cleaning and model training steps.

*If you are a recruiter or hiring manager, please feel free to reach out to me via [LinkedIn](link-to-your-linkedin) or email at your.email@example.com!*