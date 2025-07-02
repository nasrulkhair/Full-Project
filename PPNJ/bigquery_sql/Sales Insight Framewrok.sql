
-- SALE INSIGHT FRAMEWROK


SELECT *
FROM ppnj.fact_sales;

/* 1. Total Bookings & Revenue Over Time
- Understand overall performance trends 
- Power BI Visual: Line chart with dual axis for total_bookings and total_revenue by month/year. */


SELECT
  d.year,
  d.monthname,
  COUNT(fs.booking_id) total_booking,
  SUM(fs.num_of_pax * tp.price_per_pax - fs.discount_promotion) total_revenue,
  ROUND(AVG(fs.num_of_pax * tp.price_per_pax - fs.discount_promotion), 2) avg_revenue_per_booking
FROM `ppnj.fact_sales` fs
JOIN `ppnj.dim_date` d ON fs.booking_date = d.date_key
JOIN `ppnj.dim_travel_package` tp ON fs.package_id = tp.package_id
GROUP BY d.year, d.monthname
ORDER BY d.year, d.monthname;


/* 2. Top Performing Travel Packages
- Identify packages that contribute most to revenue and bookings
- Power BI Visual: Bar chart — top 10 packages by revenue or bookings. */