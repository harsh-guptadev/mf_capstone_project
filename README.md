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

## How to Run

```bash
pip install -r requirements.txt
python scripts/etl_pipeline.py