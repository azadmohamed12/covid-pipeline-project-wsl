CREATE TABLE covid_data_clean (
    location TEXT,
    date DATE,
    total_cases NUMERIC,
    total_deaths NUMERIC,
    population BIGINT
);

COPY covid_data_clean(location, date, total_cases, total_deaths, population)
FROM '/data/covid_clean.csv'
DELIMITER ','
CSV HEADER;
