import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv("data/processed/02_nav_history_cleaned.csv")

df["date"] = pd.to_datetime(df["date"])

dim_date = pd.DataFrame()
dim_date["date"] = df["date"].drop_duplicates()
dim_date["year"] = dim_date["date"].dt.year
dim_date["month"] = dim_date["date"].dt.month
dim_date["day"] = dim_date["date"].dt.day

engine = create_engine("sqlite:///bluestock_mf.db")

dim_date.to_sql(
    "dim_date",
    engine,
    if_exists="replace",
    index=False
)

print("dim_date loaded:", len(dim_date))