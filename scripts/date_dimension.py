"""
Date Dimension
---------------
Builds dim_date from the distinct dates present in the cleaned NAV
history and loads it into the SQLite database. Matches the dim_date
definition in sql/schema.sql.
"""

import pandas as pd
from sqlalchemy import create_engine

DB_PATH = "sqlite:///bluestock_mf.db"
NAV_FILE = "data/processed/02_nav_history_cleaned.csv"


def build_date_dimension(nav_file: str) -> pd.DataFrame:
    df = pd.read_csv(nav_file)
    df["date"] = pd.to_datetime(df["date"])

    dim_date = pd.DataFrame({"date": df["date"].drop_duplicates().sort_values()})
    dim_date["year"] = dim_date["date"].dt.year
    dim_date["quarter"] = "Q" + dim_date["date"].dt.quarter.astype(str)
    dim_date["month"] = dim_date["date"].dt.month
    dim_date["month_name"] = dim_date["date"].dt.month_name()
    dim_date["day"] = dim_date["date"].dt.day
    dim_date["day_of_week"] = dim_date["date"].dt.day_name()

    return dim_date.reset_index(drop=True)


def main():
    dim_date = build_date_dimension(NAV_FILE)

    engine = create_engine(DB_PATH)
    dim_date.to_sql("dim_date", engine, if_exists="replace", index=False)

    print(f"dim_date loaded: {len(dim_date)} rows "
          f"({dim_date['date'].min().date()} to {dim_date['date'].max().date()})")


if __name__ == "__main__":
    main()