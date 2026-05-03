-- COVID Summary Partitioned Table
-- Partitioned by location (country) because:
-- 1. Dashboard queries filter by country (SELECT dropdown)
-- 2. Bar chart aggregates by country
-- 3. Partitioning speeds up country-specific queries

-- Drop old table
DROP TABLE IF EXISTS covid_summary;

-- Create partitioned table
CREATE TABLE covid_summary (
    location TEXT,
    date DATE,
    total_cases DOUBLE PRECISION,
    total_deaths DOUBLE PRECISION,
    population BIGINT,
    death_rate DOUBLE PRECISION
) PARTITION BY LIST (location);

-- Country partitions
CREATE TABLE covid_summary_usa 
    PARTITION OF covid_summary FOR VALUES IN ('USA');

CREATE TABLE covid_summary_italy 
    PARTITION OF covid_summary FOR VALUES IN ('Italy');

CREATE TABLE covid_summary_germany 
    PARTITION OF covid_summary FOR VALUES IN ('Germany');

CREATE TABLE covid_summary_india 
    PARTITION OF covid_summary FOR VALUES IN ('India');

-- Default partition for any other country
CREATE TABLE covid_summary_default 
    PARTITION OF covid_summary DEFAULT;
