#!/bin/bash

# Always make sure the folder exists
mkdir -p data

echo "Step 1: Downloading data..."
curl -L -o data/covid_data.csv https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv

echo "Step 2: Done"
exit 0
