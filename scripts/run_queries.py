import sqlite3
import pandas as pd

conn = sqlite3.connect("churn.db")

with open("sql_queries/churn_analysis.sql", "r") as f:
    sql_script = f.read()

queries = [q.strip() for q in sql_script.split(";") if q.strip()]

titles = [
    "Overall Churn Metrics",
    "Churn Rate by Contract Type",
    "Churn Rate by Internet Service",
    "Churn by Tenure Cohort"
]

for title, query in zip(titles, queries):
    print("=" * 50)
    print(title)
    print("=" * 50)
    result = pd.read_sql_query(query, conn)
    print(result.to_string(index=False))
    print("\n")

conn.close()