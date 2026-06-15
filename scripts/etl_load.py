"""
ETL Load
--------
Loads the cleaned CSVs into their corresponding tables in
bluestock_mf.db. Assumes sql/schema.sql has already been
executed, so the target tables exist (and are empty for a
fresh build).
"""

import pandas as pd
from sqlalchemy import create_engine

DB_PATH = "sqlite:///bluestock_mf.db"

TABLE_SOURCES = {
    "dim_fund": "data/processed/01_fund_master_cleaned.csv",
    "fact_nav": "data/processed/02_nav_history_cleaned.csv",
    "fact_aum": "data/processed/03_aum_by_fund_house_cleaned.csv",
    "fact_performance": "data/processed/07_scheme_performance_cleaned.csv",
    "fact_transactions": "data/processed/08_investor_transactions_cleaned.csv",
}


def main():
    engine = create_engine(DB_PATH)

    for table_name, file_path in TABLE_SOURCES.items():
        df = pd.read_csv(file_path)
        df.to_sql(table_name, engine, if_exists="append", index=False)
        print(f"{table_name:<18} loaded: {len(df):>6} rows  (from {file_path})")

    print("\nAll tables loaded successfully!")


if __name__ == "__main__":
    main()