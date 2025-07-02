
CREATE TABlE ppnj.dim_date (
  date_key DATE,
  full_date DATE,
  day INT64,
  month INT64,
  monthname STRING,
  year INT64,
  weekday STRING,
  is_weekend INT64,
);


INSERT INTO `ppnj-463412.ppnj.dim_date` (
  date_key,
  full_date,
  day,
  month,
  monthname,
  year,
  weekday,
  is_weekend
)
SELECT
  d AS date_key,
  d AS full_date,
  EXTRACT(DAY FROM d) AS day,
  EXTRACT(MONTH FROM d) AS month,
  FORMAT_DATE('%B', d) AS monthname,
  EXTRACT(YEAR FROM d) AS year,
  FORMAT_DATE('%A', d) AS weekday,
  CASE WHEN EXTRACT(DAYOFWEEK FROM d) IN (1, 7) THEN 1 ELSE 0 END AS is_weekend
FROM
  UNNEST(GENERATE_DATE_ARRAY('2023-01-01', '2026-12-31', INTERVAL 1 DAY)) AS d;


SELECT *
FROM `ppnj.dim_date`
ORDER BY full_date ASC;

