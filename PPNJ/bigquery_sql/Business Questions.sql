
-- BUSINESS QUESTIONS

/* 1. Find the Top 3 Travel Packaged by Monthly Revenue Trend Per Year
- Identify which packages dominate revenue each month per year.
- Line chart with small multiples. */

SELECT * FROM `ppnj.dim_date`;

WITH monthly_revenue AS (
  SELECT 
    d.month month,
    d.year year,
    tp.package_name,
    SUM(s.num_of_pax * tp.price_per_pax - s.discount_promotion) total_revenue
  FROM `ppnj.dim_date` d 
  JOIN `ppnj.fact_sales` s ON d.date_key = s.travel_date
  JOIN `ppnj.dim_travel_package` tp ON s.package_id = tp.package_id
  GROUP BY d.year, d. month, tp.package_name
), ranked_revenue AS (
  SELECT
    *,
    RANK() OVER(PARTITION BY package_name ORDER BY total_revenue DESC) package_rank
  FROM monthly_revenue
)
SELECT *
FROM ranked_revenue
WHERE package_rank <=3;


/* 2. Find Average Discount per Channel and Usage Rate
- Understand discount impact across sales channels.
- Bar chart or matrix: Channel vs Discount rate and usage. */

SELECT
  channel,
  COUNT(*) total_bookings,
  AVG(discount_promotion) avg_discount,
  SUM(CASE WHEN discount_promotion > 0 THEN 1 ELSE 0 END) discounted_bookings,
  ROUND(SUM(CASE WHEN discount_promotion > 0 THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) dicount_usage_rate
FROM `ppnj.fact_sales` 
GROUP BY channel;

/* 3. High-Value One-Time Customers
- Identify customers who spend a lot but don't return
- Table of high spenders with only 1 booking */

WITH customer_spending AS (
  SELECT 
    c.customer_id,
    c.customer_name,
    c.customer_type,
    c.age,
    COUNT(s.booking_id) AS total_bookings,
    SUM(s.num_of_pax * tp.price_per_pax - s.discount_promotion) AS total_spent
  FROM `ppnj.fact_sales` s 
  JOIN `ppnj.dim_customers` c ON s.customer_id = c.customer_id
  JOIN `ppnj.dim_travel_package` tp ON s.package_id = tp.package_id
  GROUP BY c.customer_id, c.customer_name, c.customer_type, c.age
)
SELECT *
FROM customer_spending
WHERE total_bookings = 1
ORDER BY total_spent DESC;


/* 4. Guides with Low Ratings and High Refunds
- Identify guides underperforming based on both ratings & refund.
- Table with conditional formatting on low scores & high refunds. */

WITH guide_feedback_refund AS (
  SELECT 
    g.staff_name,
    COUNT(DISTINCT fs.booking_id) AS total_bookings,
    AVG(fb.rating_guide) AS avg_guide_rating,
    COUNT(DISTINCT r.refund_id) AS total_refunds
  FROM `ppnj.fact_sales` fs
  JOIN `ppnj.dim_travel_guide` g ON fs.guide_id = g.staff_id
  LEFT JOIN `ppnj.dim_feedback` fb ON fs.booking_id = fb.booking_id
  LEFT JOIN `ppnj.dim_refund` r ON fs.booking_id = r.booking_id
  GROUP BY g.staff_name
)
SELECT * 
FROM guide_feedback_refund
WHERE avg_guide_rating < 3 AND total_refunds > 3
ORDER BY total_refunds DESC;


/* 5. Refund Rate Among Low Satisfaction Customers
- Find out how often dissatisfied customers ask for refunds
- KPI card or bar: % of dissatisfied customers refunded */

WITH low_feedback AS (
  SELECT booking_id
  FROM `ppnj.dim_feedback`
  WHERE satisfaction_score <= 3
),
refund_stats AS (
  SELECT 
    COUNT(*) AS low_feedback_count,
    SUM(CASE WHEN r.booking_id IS NOT NULL THEN 1 ELSE 0 END) AS refunded_count
  FROM low_feedback lf
  LEFT JOIN `ppnj.dim_refund` r ON lf.booking_id = r.booking_id
)
SELECT 
  low_feedback_count,
  refunded_count,
  ROUND(refunded_count * 100.0 / low_feedback_count, 2) AS refund_rate
FROM refund_stats;

























