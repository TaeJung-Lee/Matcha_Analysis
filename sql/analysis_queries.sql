-- in terminal type:
-- sqlite3 matcha_project.db

-- .exit to exit

-- Matcha yield per hectare
SELECT year, 
       total_tencha_tons,
       tencha_field_ha,
       ROUND(total_tencha_tons / tencha_field_ha, 2) AS yield_per_ha
FROM matcha_production
ORDER BY year;

-- Compare tencha vs autumn tencha breakdown
SELECT year, 
       tencha_tons, 
       autumn_tencha_tons,
       total_tencha_tons,
       ROUND(autumn_tencha_tons / total_tencha_tons * 100.0, 1) AS autumn_percent
FROM matcha_production
WHERE total_tencha_tons > 0
ORDER BY year;

-- Total revenue from tencha (matcha-relevant)
SELECT year,
       total_tencha_yen_m,
       tencha_yen_m,
       autumn_tencha_yen_m
FROM matcha_production
ORDER BY year;

-- Tencha tons ordered by year
SELECT year, total_tencha_tons
FROM uji_matcha
ORDER BY year;


.mode csv
.headers on
.output data/cleaned_csv/final_uji_matcha_extracted.csv
SELECT * FROM uji_matcha ORDER BY year DESC;
.output stdout

.mode csv — sets output format to CSV
.headers on — includes column names in the CSV
.output [filepath] — sends results to a file
SELECT ... — your actual SQL query
.output stdout — resets output to display in terminal again