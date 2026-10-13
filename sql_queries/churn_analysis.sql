-- 1. Overall Churn Metrics (Total, Churned, Churn Rate %, ARPU)
SELECT 
    COUNT(*) AS Total_Customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS Churned_Customers,
    ROUND(SUM(CASE WHEN Churn = 'Yes' THEN 1.0 ELSE 0.0 END) / COUNT(*) * 100, 2) AS Churn_Rate_Pct,
    ROUND(AVG(MonthlyCharges), 2) AS ARPU,
    ROUND(AVG(TotalCharges), 2) AS Avg_Customer_LTV
FROM customers;

-- 2. Churn Rate by Contract Type
SELECT 
    Contract,
    COUNT(*) AS Total_Customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS Churned_Customers,
    ROUND(SUM(CASE WHEN Churn = 'Yes' THEN 1.0 ELSE 0.0 END) / COUNT(*) * 100, 2) AS Churn_Rate_Pct
FROM customers
GROUP BY Contract
ORDER BY Churn_Rate_Pct DESC;

-- 3. Churn Rate by Internet Service
SELECT 
    InternetService,
    COUNT(*) AS Total_Customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS Churned_Customers,
    ROUND(SUM(CASE WHEN Churn = 'Yes' THEN 1.0 ELSE 0.0 END) / COUNT(*) * 100, 2) AS Churn_Rate_Pct
FROM customers
GROUP BY InternetService
ORDER BY Churn_Rate_Pct DESC;

-- 4. Churn by Tenure Cohorts
SELECT 
    CASE 
        WHEN tenure <= 12 THEN '0-12 Months'
        WHEN tenure <= 24 THEN '13-24 Months'
        WHEN tenure <= 48 THEN '25-48 Months'
        ELSE '49+ Months'
    END AS Tenure_Cohort,
    COUNT(*) AS Total_Customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS Churned_Customers,
    ROUND(SUM(CASE WHEN Churn = 'Yes' THEN 1.0 ELSE 0.0 END) / COUNT(*) * 100, 2) AS Churn_Rate_Pct
FROM customers
GROUP BY Tenure_Cohort
ORDER BY Churn_Rate_Pct DESC;