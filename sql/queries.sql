SELECT * FROM fact_nav LIMIT 10;

SELECT * FROM fact_aum
ORDER BY aum_crore DESC
LIMIT 5;

SELECT AVG(nav)
FROM fact_nav;

SELECT COUNT(*)
FROM fact_transactions;

SELECT transaction_type,
COUNT(*)
FROM fact_transactions
GROUP BY transaction_type;

SELECT state,
COUNT(*)
FROM fact_transactions
GROUP BY state;

SELECT AVG(expense_ratio)
FROM fact_performance;

SELECT scheme_name,
return_5yr
FROM fact_performance
ORDER BY return_5yr DESC
LIMIT 5;

SELECT risk_grade,
COUNT(*)
FROM fact_performance
GROUP BY risk_grade;

SELECT fund_house,
COUNT(*)
FROM dim_fund
GROUP BY fund_house;