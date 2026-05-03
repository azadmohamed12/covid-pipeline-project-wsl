# 📊 COVID-19 Data Pipeline Project

## 🎯 Problem Description

The COVID-19 pandemic has been one of the most significant global health crises
in modern history, affecting millions of people across every country.
Governments, researchers, and public health organizations struggled to track
the spread of the virus and make data-driven decisions.

The challenge is that raw COVID-19 data is large, messy, and hard to analyze
without proper tooling. Analysts need a reliable, automated pipeline that:
- Collects raw COVID-19 data consistently
- Cleans and transforms it into an analyzable format
- Stores it in a structured data warehouse
- Presents insights through an interactive dashboard

This project solves that problem by building an end-to-end automated data
pipeline that ingests daily COVID-19 case and death data, loads it into
PostgreSQL, and visualizes key metrics through a Streamlit dashboard.

### ❓ Questions This Project Answers
- Which countries had the highest total COVID-19 cases?
- How did cases grow over time for each country?
- What is the maximum number of deaths recorded per country?
- How do different countries compare in case volume?

## 🏗️ Architecture
## ⚙️ Tech Stack

| Tool | Purpose |
|------|---------|
| Apache Airflow | Workflow orchestration & scheduling |
| PostgreSQL | Data warehouse |
| Docker & Docker Compose | Containerization |
| Streamlit | Interactive dashboard |
| Python | Data processing |

## 🔄 Pipeline

1. Load CSV into Postgres
2. Transform data (death rate)
3. Store in `covid_summary`

## 📊 Dashboard Features

- **Raw data table** — view all processed COVID records
- **KPI metrics** — max cases and max deaths at a glance
- **Country filter** — select any country to analyze
- **Line chart** — cases over time per country
- **Bar chart** — total cases by country

## 📋 Prerequisites

Before running this project make sure you have:
- Docker Desktop installed (version 20.10 or higher)
- Python 3.8+
- Git
- Ports **8081** (Airflow) and **5432** (Postgres) must be free

## ▶️ How to Run

### 1. Clone the repository
```bash
git clone https://github.com/azadmohamed12/covid-pipeline-project-wsl.git
cd covid-pipeline-project-wsl
```

### 2. Setup environment variables
```bash
cp .env.example .env
```

### 3. Start all services
```bash
docker compose up
```
Wait about 30 seconds for all services to start.

### 4. Setup Airflow Postgres Connection (Required!)
This step is required before triggering the DAG:
- Open http://localhost:8081 in your browser
- Login: username **admin** / password **admin**
- Go to **Admin → Connections → + Add a new record**
- Fill in:
  - **Connection Id:** postgres_default
  - **Connection Type:** Postgres
  - **Host:** postgres
  - **Database:** azad
  - **Login:** azad
  - **Password:** azad
  - **Port:** 5432
- Click **Save**

### 5. Trigger the DAG
```bash
airflow dags trigger load_data_clean
```
Or trigger manually from the Airflow UI at http://localhost:8081

### 6. Install dashboard dependencies
```bash
pip install -r requirements.txt
```

### 7. Run the dashboard
```bash
cd dashboard
streamlit run app.py
```
Open http://localhost:8501 in your browser.

## 📁 Project Structure
## 📷 Screenshots

### Airflow DAGs
![DAG 1](dashboard/screenshots/dag1.png)
![DAG 2](dashboard/screenshots/dag2.png)
![DAG 3](dashboard/screenshots/dag3.png)
![Dashboard DAG](dashboard/screenshots/dahsboard_dag.png)

### Dashboard Views
![Cases by Country](dashboard/screenshots/cases_by_country.png)
![Cases Over Time](dashboard/screenshots/cases_over_time.png)

### Processed Data
![Processed Data](dashboard/screenshots/processed_data.png)