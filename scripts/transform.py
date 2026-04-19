import os
import pandas as pd

input_path = "/opt/airflow/data/covid_data.csv"
output_path = "/opt/airflow/data/covid_clean.csv"

# delete old file if exists
if os.path.exists(output_path):
    os.remove(output_path)

df = pd.read_csv(input_path)

# your cleaning logic here
df_clean = df.dropna()

df_clean.to_csv(output_path, index=False)

print("Transform step complete: data/covid_clean.csv created")