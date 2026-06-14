import requests
import pandas as pd
from pathlib import Path
from datetime import datetime

amfi_code = "119551"

url = f"https://api.mfapi.in/mf/{amfi_code}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    latest = data["data"][0]

    output_dir = Path("data/raw/nav_updates")
    output_dir.mkdir(parents=True, exist_ok=True)

    df = pd.DataFrame([{
        "amfi_code": amfi_code,
        "scheme_name": data["meta"]["scheme_name"],
        "nav": latest["nav"],
        "date": latest["date"],
        "fetched_at": datetime.now()
    }])

    df.to_csv(
        output_dir / f"nav_update_{datetime.now().date()}.csv",
        index=False
    )

    print("NAV data fetched successfully")

else:
    print("Failed to fetch NAV")