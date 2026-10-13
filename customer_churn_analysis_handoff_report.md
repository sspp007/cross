# Project Handoff Report: Customer Churn Analysis

**Date:** October 13, 2026  
**Project Phase:** Phase 1 Complete (Data Engineering, SQL Analytics, & Predictive Modeling)  
**Estimated Project Completion:** 70%  

## 1. Project Overview
The objective of this project is to analyze customer behavior to identify the primary drivers of customer churn (cancellation of services) and to predict which current customers are at the highest risk of leaving. The project utilizes the Kaggle Telco Customer Churn dataset.

## 2. Directory Structure & File Index
The workspace has been organized into a modular structure to separate raw data, processing scripts, database files, and analytical queries.

```text
~/Desktop/CROSS/
│
├── data/
│   ├── raw/
│   │   └── WA_Fn-UseC_-Telco-Customer-Churn.csv   # Original raw dataset downloaded via Kaggle API
│   └── processed/
│       └── clean_telco_churn.csv                  # Cleaned dataset ready for SQL/ML ingestion
│
├── scripts/
│   ├── clean_data.py                              # Python script for data imputation and standardization
│   ├── load_to_sqlite.py                          # Python script that loads cleaned CSV into SQLite DB
│   ├── run_queries.py                             # Python runner for executing SQL queries
│   └── train_model.py                             # Scikit-Learn script for Random Forest churn prediction
│
├── sql_queries/
│   └── churn_analysis.sql                         # Core SQL scripts for generating business KPIs
│
└── churn.db                                       # Local SQLite database containing the 'customers' table
```

## 3. Work Performed & Completed Milestones (Phase 1)
The following tasks have been successfully completed and tested:

*   **Data Ingestion:** Automated the downloading and extraction of the Telco dataset using the Kaggle CLI API.
*   **Data Cleaning & Preprocessing (`clean_data.py`):** 
    *   Removed duplicate customer records.
    *   Handled missing values in the `TotalCharges` column (converted empty strings to NaN, cast to float, filled with 0.0).
    *   Standardized categorical columns (e.g., mapped `SeniorCitizen` from 1/0 to Yes/No).
    *   Stripped trailing/leading whitespaces from all object columns.
*   **Database Architecture (`load_to_sqlite.py`):** Established a local SQLite database (`churn.db`) and successfully loaded the processed data into the `customers` table.
*   **SQL Analytics (`churn_analysis.sql`):** Developed and executed SQL queries to extract primary Key Performance Indicators (KPIs).
    *   Calculated Overall Churn Rate (26.54%) and Average Revenue Per User (ARPU).
    *   Segmented churn by Contract Type, Internet Service, and Tenure Cohorts.
*   **Machine Learning Prediction (`train_model.py`):** Built a Random Forest Classifier using `scikit-learn` to predict churn probability and extract feature importance, proving that metrics like `Contract`, `Tenure`, and `MonthlyCharges` heavily influence churn.

## 4. Key Analytical Findings
The data analysis has revealed several critical insights for the business so far:
1.  **Contract Vulnerability:** Month-to-month contracts have an aggressively high churn rate of 42.71%, compared to just 2.83% for two-year contracts.
2.  **Product Issue:** Customers utilizing Fiber Optic internet services churn at a much higher rate (41.89%) than DSL users (18.96%).
3.  **High-Risk Window:** The first 12 months are the most critical, with a 47.44% churn rate. Retention stabilizes significantly after the first year.

## 5. Pending Work & Next Steps (Phase 2 - Handoff Tasks)
The remaining 30% of the project involves Business Intelligence (BI), visualization, and final presentation. The next person taking over should focus on:

*   **[ ] Step 1: Connect BI Tool to Data Source:** Connect Tableau Desktop (or Power BI) directly to the `churn.db` SQLite database or the `clean_telco_churn.csv` file.
*   **[ ] Step 2: Build the Dashboard:**
    *   Create KPI cards for Total Customers, Churn Rate, and Monthly Revenue.
    *   Build a line/bar chart showing Churn by Contract Type and Internet Service.
    *   Implement interactive slicers/filters for Gender, Payment Method, and Tenure Group.
*   **[ ] Step 3: Integrate ML Outputs (Optional but Recommended):** Export the churn probability predictions from the Random Forest model and visualize "At-Risk Customers" in the dashboard.
*   **[ ] Step 4: Business Insights Documentation:** Draft the final business recommendations based on the dashboard visuals (e.g., "Incentivize 1-year contracts for Fiber Optic users").
*   **[ ] Step 5: Final Deployment:** Publish the completed dashboard to Tableau Public and update the GitHub `README.md` with screenshots and the live link.