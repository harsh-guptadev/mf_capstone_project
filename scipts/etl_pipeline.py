 import pandas as pd
from pathlib import Path

data_path = Path("data/raw")

csv_files = list(data_path.glob("*.csv"))

print(f"Found {len(csv_files)} CSV files\n")

for file in csv_files:
    df = pd.read_csv(file)
    print("Missing Values")
    print(df.isnull().sum())

    print("=" * 50)
    print("File:", file.name)
    print("Shape:", df.shape)
    print("\nColumns:")
    print(df.columns.tolist())
    print("\nData Types:")
    print(df.dtypes)
    print("\nFirst 5 Rows:")
    print(df.head())
    print("\n") 
import sqlite3

conn = sqlite3.connect("bluestock_mf.db")

with open("sql/schema.sql", "r") as f:
    sql_script = f.read()

conn.executescript(sql_script)

print("Tables created successfully!")

conn.close()