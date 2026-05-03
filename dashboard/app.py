import streamlit as st
import pandas as pd
import psycopg2
import os

# CONNECT TO SUPABASE
conn = psycopg2.connect(
    host="aws-1-eu-central-1.pooler.supabase.com",
    database="postgres",
    user="postgres.cfhlplwncfryzbtunngo",
    password="Pg!9xT#7vQz@4LmN2wRb",
    port=5432
)

# LOAD DATA
query = "SELECT * FROM covid_summary;"
df = pd.read_sql(query, conn)

# UI
st.title("📊 COVID Dashboard")

st.subheader("Processed Data")
st.dataframe(df)

# KPI
st.subheader("Key Metrics")
col1, col2 = st.columns(2)
col1.metric("Max Cases", int(df["total_cases"].max()))
col2.metric("Max Deaths", int(df["total_deaths"].max()))

# FILTER
selected_country = st.selectbox("Select Country", df["location"].unique())
filtered_df = df[df["location"] == selected_country].sort_values("date")

# LINE CHART
st.subheader("Cases Over Time")
st.line_chart(filtered_df.set_index("date")["total_cases"])

# BAR CHART
st.subheader("Total Cases by Country")
country_df = df.groupby("location")["total_cases"].max()
st.bar_chart(country_df)

conn.close()
