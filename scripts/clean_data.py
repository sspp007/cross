import pandas as pd
import numpy as np

raw_path = "data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv"
processed_path = "data/processed/clean_telco_churn.csv"

# 1. Load data
df = pd.read_csv(raw_path)
print(f"Initial shape: {df.shape}")

# 2. Check and drop duplicate customers
df = df.drop_duplicates(subset=["customerID"])

# 3. Clean 'TotalCharges': replace blank strings with NaN, convert to float, then fill with 0
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"].str.strip(), errors="coerce")
df["TotalCharges"] = df["TotalCharges"].fillna(0.0)

# 4. Standardize 'SeniorCitizen' to Yes/No to match other categorical columns
df["SeniorCitizen"] = df["SeniorCitizen"].map({1: "Yes", 0: "No"})

# 5. Strip any accidental whitespace from categorical columns
categorical_cols = df.select_dtypes(include=["object"]).columns
for col in categorical_cols:
    df[col] = df[col].astype(str).str.strip()

# 6. Save cleaned data
df.to_csv(processed_path, index=False)
print(f"Cleaned dataset saved to: {processed_path}")
print(f"Final shape: {df.shape}")
print("Data types summary:")
print(df.dtypes[["customerID", "tenure", "MonthlyCharges", "TotalCharges", "Churn"]])