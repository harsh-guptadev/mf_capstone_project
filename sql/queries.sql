#1
SELECT * FROM fact_nav LIMIT 10;
#2
SELECT * FROM fact_aum
ORDER BY aum_crore DESC
LIMIT 5;
#3
SELECT AVG(nav)
FROM fact_nav;
#4
SELECT COUNT(*)
FROM fact_transactions;
#5
SELECT transaction_type,
COUNT(*)
FROM fact_transactions
GROUP BY transaction_type;

#6 
SELECT state,
COUNT(*)
FROM fact_transactions
GROUP BY state;
#7
SELECT AVG(expense_ratio)
FROM fact_performance;
#8
SELECT scheme_name,
return_5yr
FROM fact_performance
ORDER BY return_5yr DESC
LIMIT 5;
WITH ranked_funds AS (
    SELECT f.scheme_name,
           f.fund_house,
           f.category,
           p.return_3yr_pct,
           RANK() OVER (
               PARTITION BY f.category
               ORDER BY p.return_3yr_pct DESC
           ) AS category_rank
    FROM fact_performance p
    JOIN dim_fund f ON f.amfi_code = p.amfi_code
)
#9
SELECT category, scheme_name, fund_house, return_3yr_pct
FROM ranked_funds
WHERE category_rank = 1
ORDER BY return_3yr_pct DESC;
#10
SELECT f.risk_category,
       COUNT(*) AS num_schemes,
       ROUND(AVG(p.return_3yr_pct), 2) AS avg_return_3yr_pct,
       ROUND(AVG(p.std_dev_ann_pct), 2) AS avg_volatility_pct
FROM fact_performance p
JOIN dim_fund f ON f.amfi_code = p.amfi_code
GROUP BY f.risk_category
ORDER BY avg_volatility_pct DESC;