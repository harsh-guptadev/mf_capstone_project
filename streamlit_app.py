import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Mutual Fund Analytics", layout="wide")

st.title("Mutual Fund Analytics Dashboard")

fund = pd.read_csv("data/processed/01_fund_master_cleaned.csv")
aum = pd.read_csv("data/processed/03_aum_by_fund_house_cleaned.csv")
performance = pd.read_csv("data/processed/07_scheme_performance_cleaned.csv")

st.header("Project Overview")

col1, col2, col3 = st.columns(3)

col1.metric("Total Funds", len(fund))

if "aum_crore" in aum.columns and "date" in aum.columns:
    latest_date = aum["date"].max()
    latest_aum = aum.loc[aum["date"] == latest_date, "aum_crore"].sum()
    col2.metric(f"Total AUM (\u20B9 Cr, as of {latest_date})", f"{latest_aum:,.0f}")

if "scheme_name" in fund.columns:
    col3.metric("Unique Schemes", fund["scheme_name"].nunique())

st.divider()

st.header("Top Performing Funds")

if "return_1yr_pct" in performance.columns:

    top_funds = performance.sort_values(
        by="return_1yr_pct",
        ascending=False
    ).head(10)

    st.dataframe(top_funds)

    fig = px.bar(
        top_funds,
        x="scheme_name",
        y="return_1yr_pct",
        title="Top 10 Funds by 1Y Return (%)"
    )

    st.plotly_chart(fig, use_container_width=True)

st.divider()

st.header("Category Distribution")

if "category" in fund.columns:

    cat_count = fund["category"].value_counts()

    fig = px.pie(
        values=cat_count.values,
        names=cat_count.index,
        title="Fund Categories"
    )

    st.plotly_chart(fig, use_container_width=True)

st.divider()

st.header("Alpha vs Beta Analysis")

if "alpha" in performance.columns and "beta" in performance.columns:

    fig = px.scatter(
        performance,
        x="beta",
        y="alpha",
        hover_name="scheme_name",
        title="Alpha vs Beta"
    )

    st.plotly_chart(fig, use_container_width=True)

st.divider()

st.header("Performance Dataset")

st.dataframe(performance.head(50))
