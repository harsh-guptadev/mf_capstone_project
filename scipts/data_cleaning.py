import pandas as pd
from pathlib import Path

raw_path = Path("data/raw")
processed_path = Path("data/processed")

processed_path.mkdir(parents=True, exist_ok=True)

for file in raw_path.glob("*.csv"):
    print(f"Processing {file.name}")

    df = pd.read_csv(file)

    df = df.drop_duplicates()

    for col in df.columns:
        if "date" in col.lower():
            try:
                df[col] = pd.to_datetime(df[col])
            except:
                pass

    cleaned_name = file.stem + "_cleaned.csv"

    df.to_csv(
        processed_path / cleaned_name,
        index=False
    )

    print(f"Saved: {cleaned_name}")

print("All files cleaned successfully!")