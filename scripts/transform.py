import os
import sys
import pandas as pd

input_path = "/opt/airflow/data/covid_data.csv"
output_path = "/opt/airflow/data/covid_clean.csv"

if not os.path.exists(input_path):
    raise FileNotFoundError("Input file missing — ingest failed")
else:
    df = pd.read_csv(input_path)
    df_clean = df.dropna()
    df_clean.to_csv(output_path, index=False)
    print("Transform complete")