# Bluestock Mutual Fund Analytics - Capstone Project

An end-to-end data analytics pipeline for the Indian mutual fund industry: raw CSV data is cleaned, validated, and loaded into a SQLite star-schema database, then analyzed through Python notebooks, a Power BI dashboard, and a Streamlit web app.

## Objective

Build a complete analytics pipeline that takes raw mutual fund data and turns it into business-ready insights:

- Ingest and clean 10 raw datasets covering funds, NAV history, AUM, SIP inflows, and investor transactions
- Load the cleaned data into a structured SQLite database (star schema)
- Perform exploratory, performance, and advanced analytics (correlation, ranking, sector allocation)
- Visualize results in an interactive Power BI dashboard and a Streamlit app
- Automate recurring tasks: NAV updates and a weekly HTML report

## Tech Stack

- **Python** - pandas, NumPy, SciPy
- **SQLite** + **SQLAlchemy** - database and ORM-style loading
- **Power BI** - interactive dashboard
- **Streamlit** + **Plotly** - web-based analytics app
- **Matplotlib / Seaborn** - static chart generation
- **Git & GitHub** - version control

## Project Structure

```
mf_capstone_project/
├── data/
│   ├── raw/                    # 10 original CSV datasets + nav_updates/
│   └── processed/              # Cleaned datasets (output of data_cleaning.py)
├── scripts/
│   ├── data_cleaning.py        # Cleans, deduplicates, fills missing values
│   ├── etl_load.py             # Loads cleaned data into SQLite
│   ├── date_dimension.py       # Builds the dim_date table
│   ├── amfi_validation.py      # Validates AMFI code coverage
│   ├── etl_pipeline.py         # Orchestrates the full pipeline (run this)
│   ├── nav_auto_fetch.py        # Bonus: live NAV fetch from api.mfapi.in
│   └── html_report.py           # Bonus: auto-generates an HTML report
├── sql/
│   ├── schema.sql               # Database schema (DDL)
│   └── queries.sql              # Analysis queries (joins, CTEs, window functions)
├── notebooks/
│   ├── 03_eda_analysis.ipynb
│   ├── 04_performance_analytics.ipynb
│   └── 05_advanced_analytics.ipynb
├── dashboard/                    # Power BI file (.pbix) + exported chart images
├── dashboard_data/                # Aggregated CSVs feeding the dashboard
├── reports/                       # Final report, presentation, dashboard screenshots
├── streamlit_app.py               # Bonus: Streamlit web dashboard
├── requirements.txt
└── README.md
```

## Dataset Description

| # | Dataset | Purpose |
|---|---------|---------|
| 1 | Fund Master | Scheme information (fund house, category, manager, fees) |
| 2 | NAV History | Historical daily NAV per scheme |
| 3 | AUM by Fund House | Assets under management over time |
| 4 | Monthly SIP Inflows | SIP contribution trends |
| 5 | Category Inflows | Net inflows by fund category |
| 6 | Industry Folio Count | Investor folio growth |
| 7 | Scheme Performance | Returns, risk metrics, ratings |
| 8 | Investor Transactions | Transaction-level investor activity |
| 9 | Portfolio Holdings | Sector allocation of fund portfolios |
| 10 | Benchmark Indices | Index values for performance comparison |

## ETL Pipeline

`scripts/etl_pipeline.py` runs the full pipeline end-to-end and is safe to re-run (it rebuilds the database from scratch each time):

1. **Clean** - `data_cleaning.py` removes duplicates, parses date columns, and fills missing values (numeric columns get the column median, text columns get `"Unknown"`).
2. **Schema** - rebuilds `bluestock_mf.db` from `sql/schema.sql`.
3. **Load** - `etl_load.py` loads the cleaned CSVs into `dim_fund`, `fact_nav`, `fact_aum`, `fact_performance`, and `fact_transactions`.
4. **Date dimension** - `date_dimension.py` builds `dim_date` (year, quarter, month, day, day of week) from the NAV history dates.
5. **Validation** - `amfi_validation.py` confirms every fund in `dim_fund` has matching NAV history.

## Database Schema

Star schema with two dimension tables and four fact tables, linked on `amfi_code` and `date`:

| Table | Type | Key Columns |
|-------|------|-------------|
| `dim_fund` | Dimension | amfi_code (PK), fund_house, scheme_name, category, expense_ratio_pct, risk_category |
| `dim_date` | Dimension | date (PK), year, quarter, month, day, day_of_week |
| `fact_nav` | Fact | amfi_code, date, nav |
| `fact_aum` | Fact | date, fund_house, aum_crore, num_schemes |
| `fact_performance` | Fact | amfi_code, return_1yr_pct, return_3yr_pct, alpha, beta, sharpe_ratio, max_drawdown_pct |
| `fact_transactions` | Fact | investor_id, transaction_date, amfi_code, amount_inr, state, age_group, gender |

See `sql/queries.sql` for analysis queries, including joins across `dim_fund`, ranking funds with `RANK() OVER (...)`, and a CTE that finds the top fund per category.

## Analysis & Key Insights

**Exploratory Data Analysis** (`notebooks/03_eda_analysis.ipynb`)
- Investors aged 26-35 form the largest segment (41% of the base); 18-45 year-olds make up over 80% of all investors.
- Male investors represent 66.5% of the base vs. 33.5% female.
- Punjab, Tamil Nadu, and Madhya Pradesh lead all states by total investment amount.

**Performance Analytics** (`notebooks/04_performance_analytics.ipynb`)
- Across 40 schemes from 10 fund houses, the average 3-year return is 14.09% with an average Sharpe ratio of 1.36.
- Average Alpha of 1.25 and Beta of 0.87 indicate funds are generating excess returns with below-market volatility.

**Advanced Analytics** (`notebooks/05_advanced_analytics.ipynb`)
- Sector allocation is led by Banking (19.2%), IT (13.4%), and Pharma (12.0%).
- NAV return correlations across top funds are generally low, suggesting healthy diversification.
- SBI Mutual Fund leads in average AUM, followed by ICICI Prudential and HDFC.

## Power BI Dashboard

`dashboard/bluestock_mf.pbix` contains five pages:

1. **Industry Overview** - total funds, schemes, fund houses, and average expense ratio
2. **Fund Performance** - top fund houses by 3-year return, risk vs. return scatter
3. **Investor & SIP Analysis** - investor count, SIP inflow trends, transaction breakdown
4. **Market Trends** - SIP inflows and benchmark trends by category
5. **Executive Summary** - total AUM, average return, average Sharpe ratio, top schemes

Screenshots of each page are in `reports/screenshort/`.

## Bonus: Streamlit Web App

An interactive alternative to the Power BI dashboard, built with Streamlit and Plotly:

- Project overview metrics (total funds, latest AUM, unique schemes)
- Top 10 funds by 1-year return
- Fund category distribution
- Alpha vs. Beta scatter plot
- Searchable performance dataset

Run locally:

```bash
streamlit run streamlit_app.py
```

## Bonus: Automated NAV Fetching

`scripts/nav_auto_fetch.py` fetches the latest NAV for a given AMFI code from the [MFAPI](https://www.mfapi.in/) API and appends it to `data/raw/nav_updates/`, timestamped. See `reports/etl_scheduler.md` for how to schedule it with Windows Task Scheduler.

## Bonus: Automated HTML Report

`scripts/html_report.py` generates `reports/weekly_report.html`, a self-contained HTML summary embedding the key chart images from `dashboard/`.

## How to Run

```bash
# 1. Clone and set up the environment
git clone https://github.com/harsh-guptadev/mf_capstone_project.git
cd mf_capstone_project
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# 2. Run the full ETL pipeline (clean -> schema -> load -> date dimension -> validate)
python scripts/etl_pipeline.py

# 3. Explore the database
sqlite3 bluestock_mf.db
.read sql/queries.sql

# 4. Launch the Streamlit dashboard
streamlit run streamlit_app.py

# 5. (Optional) Fetch a live NAV update
python scripts/nav_auto_fetch.py

# 6. (Optional) Regenerate the HTML report
python scripts/html_report.py
```

The Power BI dashboard (`dashboard/bluestock_mf.pbix`) can be opened directly in Power BI Desktop.

## Future Enhancements

- Real-time NAV updates via a scheduled job (cron / Task Scheduler)
- Predictive fund return modeling with machine learning
- Cloud deployment of the Streamlit app (e.g., Streamlit Community Cloud)
- CI pipeline to run the ETL and basic data-quality checks on every push
