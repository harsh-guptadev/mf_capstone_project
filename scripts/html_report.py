from pathlib import Path

html = """
<!DOCTYPE html>
<html>
<head>
<title>Mutual Fund Weekly Report</title>
<style>
body{
font-family:Arial;
margin:40px;
}
h1{
color:#2c3e50;
}
img{
width:700px;
margin:20px 0;
border:1px solid #ddd;
}
</style>
</head>
<body>

<h1>Mutual Fund Performance Report</h1>

<h2>Top Funds</h2>
<img src="../dashboard/top5_funds.png">

<h2>AUM Growth</h2>
<img src="../dashboard/aum_growth.png">

<h2>Sector Allocation</h2>
<img src="../dashboard/sector_allocation.png">

<h2>State Distribution</h2>
<img src="../dashboard/state_distribution.png">

<p>Generated automatically using Python.</p>

</body>
</html>
"""

Path("reports").mkdir(exist_ok=True)

with open("reports/weekly_report.html","w",encoding="utf-8") as f:
    f.write(html)

print("HTML Report Created")