
-- CUSTOMER BEHAVIOR INSIGHT FRAMEWORK

/* 1. Customer Demographic Profile
- Understand age, gender, and type of typical customer
-- Visual: Stacked bar chart by gender and customer_type / Card for avg_age. */

SELECT 
  gender,
  customer_type,
  COUNT(customer_id) total_customers,
  ROUND(AVG(age),0) avg_age
FROM `ppnj.dim_customers`
GROUP BY gender, customer_type;


/* 2. Preferred Package Name by Traveller type
- Identify which packages attract which traveller types (e.g., solo, family, couple)
- Matrix table or heatmap — package_name vs. customer_type */

SELECT
  tp.package_name,
  tp.package_type,
  COUNT(s.booking_id) total_booking
FROM `ppnj.fact_sales` s
JOIN `ppnj.dim_travel_package` tp ON s.package_id = tp.package_id
JOIN `ppnj.dim_customers` c ON s.customer_id = c.customer_id
GROUP BY tp.package_type, tp.package_name;


/* 3. Repeat vs. New Customers
- Track Customer loyalty
- Donut chart — new vs. repeat. */

-- 1st option
SELECT
  customer_type,
  COUNT(*) total_customer
FROM `ppnj.dim_customers`
GROUP BY customer_type;

-- 2nd option
SELECT 
  CASE
    WHEN booking_count > 1 THEN 'repeat' 
    ELSE 'new'
  END customer_status,
  COUNT(*) num_customers
FROM (
  SELECT
    customer_id,
    COUNT(*) booking_count
  FROM `ppnj.fact_sales`
  GROUP BY customer_id
) sub
GROUP BY customer_status;

/* the result might diverge because the status in customer_type column is updated from historical data,
to find the exact of new/repeat customers use the 2nd option query */

