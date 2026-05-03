-- Staging model: clean and rename raw covid data
SELECT
    location,
    date,
    total_cases,
    total_deaths,
    population
FROM {{ source('public', 'covid_table') }}
WHERE total_cases IS NOT NULL
AND location IS NOT NULL
