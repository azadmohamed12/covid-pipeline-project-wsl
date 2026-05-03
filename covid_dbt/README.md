Welcome to your new dbt project!

### Using the starter project

Try running the following commands:
- dbt run
- dbt test


### Resources:
- Learn more about dbt [in the docs](https://docs.getdbt.com/docs/introduction)
- Check out [Discourse](https://discourse.getdbt.com/) for commonly asked questions and answers
- Join the [chat](https://community.getdbt.com/) on Slack for live discussions and support
- Find [dbt events](https://events.getdbt.com) near you
- Check out [the blog](https://blog.getdbt.com/) for the latest news on dbt's development and best practices

## 🔄 Transformations (dbt)

This project uses **dbt (Data Build Tool)** to transform raw COVID-19 
data into clean, analytical models. dbt organizes SQL transformations 
into separate, testable, and documented models.

### 🏗️ Model Structure

### 📋 Models

**Staging** (`models/staging/stg_covid.sql`)
Cleans raw COVID data by filtering null values and selecting 
relevant columns.

**Mart** (`models/marts/fct_covid_summary.sql`)
Final analytical model that adds death rate calculation on top 
of the staging model.

### ✅ Data Quality Tests

| Test | Model | Result |
|------|-------|--------|
| not_null | stg_covid.location | ✅ PASS |
| not_null | stg_covid.date | ✅ PASS |
| not_null | fct_covid_summary.location | ✅ PASS |
| not_null | fct_covid_summary.death_rate | ✅ PASS |
