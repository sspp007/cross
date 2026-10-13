import sqlite3
import pandas as pd

# Load cleaned data
csv_path = "data/processed/clean_telco_churn.csv"
db_path = "churn.db"

df = pd.read_csv(csv_path)

# Connect to SQLite (creates the file if it doesn't exist)
conn = sqlite3.connect(db_path)

# Write to table 'customers'
df.to_sql("customers", conn, if_exists="replace", index=False)

# Verify count
cursor = conn.cursor()
cursor.execute("SELECT COUNT(*) FROM customers;")
count = cursor.fetchone()[0]

print(f"Successfully loaded {count} rows into table 'customers' in {db_path}.")
conn.close()