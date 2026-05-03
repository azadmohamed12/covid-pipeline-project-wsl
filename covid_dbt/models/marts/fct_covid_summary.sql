-- Final model: add death rate calculation
SELECT
    location,
    date,
    total_cases,
    total_deaths,
    population,
    (total_deaths / NULLIF(population, 0)) * 100 AS death_rate
FROM {{ ref('stg_covid') }}
