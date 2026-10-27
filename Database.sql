WITH CleanedTelco AS (
    -- 1. Data Cleaning: Convert blank TotalCharges to NULL and cast to numeric types
    SELECT 
        customerID,
        gender,
        tenure,
        Contract,
        MonthlyCharges,
        -- Handle the blank space issue present in the raw CSV
        CAST(NULLIF(TRIM(TotalCharges), '') AS DECIMAL) AS TotalCharges,
        Churn
    FROM telco_customer_churn
),
FeatureEngineering AS (
    -- 2. Feature Creation: Use Window Functions for business logic
    SELECT 
        customerID,
        tenure,
        Contract,
        MonthlyCharges,
        TotalCharges,
        Churn,
        -- Flag premium users paying more than $70
        CASE WHEN MonthlyCharges > 70.00 THEN 1 ELSE 0 END AS is_premium,
        -- Calculate the average monthly charge grouped by contract type
        AVG(MonthlyCharges) OVER(PARTITION BY Contract) AS avg_contract_charge
    FROM CleanedTelco
    WHERE TotalCharges IS NOT NULL
)
-- 3. Final Output: Calculate charge differences to find overpaying customers
SELECT 
    customerID,
    tenure,
    Contract,
    MonthlyCharges,
    TotalCharges,
    is_premium,
    ROUND(avg_contract_charge, 2) AS avg_contract_charge,
    ROUND((MonthlyCharges - avg_contract_charge), 2) AS charge_difference,
    Churn
FROM FeatureEngineering;