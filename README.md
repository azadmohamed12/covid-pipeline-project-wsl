# 📊 COVID Data Pipeline Project

## 🎯 Problem

This project analyzes COVID-19 trends across countries, focusing on case growth and death rates over time.

## 🏗️ Architecture

CSV Data (data folder) → Airflow DAG → PostgreSQL → Streamlit Dashboard

## ⚙️ Tech Stack

* Airflow (orchestration)
* Postgres (data warehouse)
* Docker
* Streamlit

## 🔄 Pipeline

1. Load CSV into Postgres
2. Transform data (death rate)
3. Store in `covid_summary`

## 📊 Dashboard

* Line chart: cases over time
* Bar chart: cases by country

## ▶️ How to Run

```bash
docker compose up
```

Trigger DAG:

```bash
airflow dags trigger load_data_clean
```

Run dashboard:

```bash
cd dashboard
streamlit run app.py
```

## 📁 Project Structure

* dags/ → pipeline
* data/ → data lake (CSV)
* dashboard/ → UI
