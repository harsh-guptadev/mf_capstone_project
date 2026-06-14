# Bluestock Mutual Fund Capstone Project

## Project Overview
Brief description of the project and objectives.

## Dataset Description
- Fund Master
- NAV History
- AUM by Fund House
- Monthly SIP Inflows
- Category Inflows
- Industry Folio Count
- Scheme Performance
- Investor Transactions
- Portfolio Holdings
- Benchmark Indices

## Project Structure

(paste your folder structure)

## ETL Pipeline
- Data ingestion
- Data cleaning
- Validation
- SQLite loading

## Database Schema
List tables:
- dim_date
- dim_fund
- fact_nav
- fact_aum
- fact_performance
- fact_transactions

## Exploratory Data Analysis
Key findings from EDA.

## Performance Analytics
- CAGR
- Sharpe Ratio
- Alpha
- Beta
- Volatility
- Maximum Drawdown

## Advanced Analytics
- Correlation Analysis
- Fund Ranking
- Sector Analysis

## Power BI Dashboard
Page 1 – Industry Overview
Page 2 – Fund Performance
Page 3 – Inventory & SIP Analysis
Page 4 – SIP & Market Trends
Page 5 – Executive Summary
## Dashboard Screenshots

### Power BI Dashboard
![Page1](reports/screenshort/page1_industry_overview.png)

### Streamlit Dashboard
![Streamlit](reports/screenshort/streamlit_dashboard_1.png)

## How to Run

```bash
pip install -r requirements.txt
python scripts/etl_pipeline.py

## Bonus Challenge – Streamlit Web Application

An interactive Streamlit dashboard was developed as an alternative to Power BI.

Features:
- Fund Overview
- Top Performing Funds
- Category Distribution
- Alpha-Beta Analysis
- Interactive Visualizations
- Performance Dataset Explorer

Run locally:

python -m streamlit run streamlit_app.py
## Bonus Challenge B2 - Streamlit Dashboard

Interactive dashboard built using Streamlit for mutual fund analytics.

Run:

streamlit run streamlit_app.py

## Bonus Challenge B5 - Automated HTML Report

Generated an HTML report automatically from analytics outputs and visualizations.

Output:
reports/weekly_report.html
## Bonus Challenge B1 – Automated NAV Fetching

Implemented an automated NAV fetching system using MFAPI.

Features:
- Fetches latest NAV using AMFI codes
- Stores results in CSV format
- Records fetch timestamp
- Can be scheduled using Windows Task Scheduler
- Supports integration with ETL pipeline

Output:
data/raw/nav_updates/
