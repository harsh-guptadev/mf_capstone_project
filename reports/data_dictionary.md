# Mutual Fund Analytics Data Dictionary

## dim_fund
- amfi_code: Unique mutual fund identifier
- fund_house: Asset management company
- scheme_name: Name of mutual fund scheme
- category: Fund category
- sub_category: Detailed category
- plan: Regular or Direct plan
- launch_date: Scheme launch date
- benchmark: Benchmark index
- expense_ratio_pct: Expense ratio percentage

## dim_date
- date: Calendar date
- year: Year
- month: Month number
- day: Day number

## fact_nav
- amfi_code: Fund identifier
- date: NAV date
- nav: Net Asset Value

## fact_aum
- date: Reporting date
- fund_house: Fund house name
- aum_crore: Assets Under Management (Crores)
- num_schemes: Number of schemes

## fact_performance
- amfi_code: Fund identifier
- return_1yr: 1 year return
- return_3yr: 3 year return
- return_5yr: 5 year return
- expense_ratio: Expense ratio
- risk_grade: Risk classification

## fact_transactions
- investor_id: Investor identifier
- transaction_type: SIP/Lumpsum/Redemption
- amount_inr: Transaction amount
- state: Investor state
- city: Investor city
- payment_mode: Payment method
- kyc_status: KYC verification status