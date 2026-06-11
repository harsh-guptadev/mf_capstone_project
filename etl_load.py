import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///bluestock_mf.db")

files = {
    "dim_fund": "data/processed/01_fund_master_cleaned.csv",
    "fact_nav": "data/processed/02_nav_history_cleaned.csv",
    "fact_aum": "data/processed/03_aum_by_fund_house_cleaned.csv",
    "fact_performance": "data/processed/07_scheme_performance_cleaned.csv",
    "fact_transactions": "data/processed/08_investor_transactions_cleaned.csv"
}

for table_name, file_path in files.items():
    df = pd.read_csv(file_path)

    df.to_sql(
        table_name,
        engine,
        if_exists="append",
        index=False
    )

    print(f"{table_name} loaded : {len(df)} rows")

print("All tables loaded successfully!")