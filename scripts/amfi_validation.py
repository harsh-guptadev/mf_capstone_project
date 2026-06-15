import pandas as pd

FUND_MASTER_FILE = "data/raw/01_fund_master.csv"
NAV_HISTORY_FILE = "data/raw/02_nav_history.csv"
def main():
    fund_master = pd.read_csv(FUND_MASTER_FILE)
    nav_history = pd.read_csv(NAV_HISTORY_FILE)

    fund_codes = set(fund_master["amfi_code"])
    nav_codes = set(nav_history["amfi_code"])

    missing_codes = fund_codes - nav_codes

    print(f"Fund Master Codes: {len(fund_codes)}")
    print(f"NAV History Codes: {len(nav_codes)}")
    print(f"Missing Codes:     {len(missing_codes)}")

    if not missing_codes:
        print("All AMFI codes in fund master have matching NAV history.")
    else:
        print("Codes in fund master with no NAV history:")
        print(sorted(missing_codes))


if __name__ == "__main__":
    main()
