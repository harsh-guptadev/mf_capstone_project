CREATE TABLE dim_fund (
    amfi_code INTEGER PRIMARY KEY,
    fund_house TEXT,
    scheme_name TEXT,
    category TEXT,
    sub_category TEXT,
    plan TEXT,
    launch_date DATE,
    benchmark TEXT,
    expense_ratio_pct REAL,
    exit_load_pct REAL,
    min_sip_amount REAL, 
    min_lumpsum_amount REAL,
    fund_manager TEXT,s
    risk_category TEXT,
    sebi_category_code TEXT
);
CREATE TABLE Fact_nav(
    amfi_code INTEGER,
    date DATE,
    nav REAL,
    FOREIGN KEY (amfi_code)
    REFERENCES dim_fund(amfi_code)
);
CREATE TABLE dim_date(
    date DATE PRIMARY KEY,
    year INTEGER,
    month INTEGER,
    quarter TEXT
);
CREATE TABLE fact_aum (
    date DATE,
    fund_house TEXT,
    aum_lakh_crore REAL,
    aum_crore REAL,
    num_schemes INTEGER,

    FOREIGN KEY (date)
    REFERENCES dim_date(date)
);
CREATE TABLE fact_performance (
    amfi_code INTEGER,
    return_1yr REAL,
    return_3yr REAL,
    return_5yr REAL,
    benchmark_return REAL,
    alpha REAL,
    beta REAL,
    sharpe_ratio REAL,
    sortino_ratio REAL,
    std_dev REAL,
    max_drawdown REAL,
    aum_crore REAL,
    expense_ratio REAL,
    morningstar_rating INTEGER,
    risk_grade INTEGER,
    risk_category TEXT,

    FOREIGN KEY (amfi_code)
    REFERENCES dim_fund(amfi_code)
);
CREATE TABLE fact_transactions (
    investor_id TEXT,
    transaction_date DATE,
    amfi_code INTEGER,
    transaction_type TEXT,
    amount_invested REAL,
    state TEXT,
    city TEXT,
    city_tier TEXT,
    age_group TEXT,
    gender TEXT,
    annual_income REAL,
    payment_mode TEXT,
    kyc_status TEXT,

    FOREIGN KEY (amfi_code)
    REFERENCES dim_fund(amfi_code)
);

