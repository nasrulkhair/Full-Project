
-- Market Analysis: Price Trends --

-- For checking
SELECT *
FROM power_bi_import


-- Market Analysis: Price Trends

-- 1. What is the average price/sqft for each propert type and land status
SELECT
	property_type,
	land_status,
	AVG(prices) as Average_price
FROM power_bi_import
GROUP BY property_type, land_status

-- 2. Whcich location has the highest median property price for landed properties?

WITH Median_CTE AS (
    SELECT 
        location,
        PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY prices) 
            OVER (PARTITION BY location) AS Median_Price
    FROM power_bi_import
    WHERE property_type = 'landed'
)
SELECT DISTINCT location, Median_Price
FROM Median_CTE
ORDER BY Median_Price DESC;


-- Demand & Supply Insights

-- 3. Which property type is most common in each district?

SELECT
	property_type,
	COUNT(*) total_listings
FROM power_bi_import
GROUP BY property_type
ORDER BY total_listings DESC

-- 4. What is the average number of bedrooms and bathrooms per property_type

SELECT 
	property_type,
	ROUND(AVG(total_bedroom),0) average_bedroom,
	ROUND(AVG(total_bathroom),0) average_bathroom
FROM power_bi_import
GROUP BY property_type

-- 5. Which land status is more common in each district?

SELECT DISTINCT(land_status) FROM power_bi_import

SELECT
	land_status,
	COUNT(*) major_listing
FROM power_bi_import
GROUP BY land_status


-- Affordability & Investment Insights

-- 6. Which districts offers the best price per bedroom for buyers?

SELECT
	location,
	ROUND(AVG(prices / NULLIF(total_bedroom,0)), 2) price_per_bedroom
FROM power_bi_import
GROUP BY location
ORDER BY price_per_bedroom

-- 7. What is the price difference between Freehold and Leasehold properties?

SELECT 
	property_type,
	land_status,
	AVG(prices) avg_price
FROM power_bi_import
GROUP BY property_type, land_status

-- 8. Which properties offer the best price per sq/ft under RM500k

SELECT
	location,
	property_type,
	prices,
	size_sqft,
	prices/ NULLIF(size_sqft, 0) price_sqft
FROM power_bi_import
WHERE prices <= 500000
ORDER BY price_sqft ASC

-- Outliers & Anomalies Detection

-- 9. Are there any properties with abnormally high or low prices compared to the average?

SELECT * 
FROM power_bi_import
WHERE prices > ( SELECT AVG(prices) * 2 FROM power_bi_import)
	OR prices < (SELECT AVG(prices) / 2 FROM power_bi_import)

-- 10. Which properties have an unusually high number of bedrooms compared to their size?

SELECT * 
FROM power_bi_import
WHERE total_bedroom / NULLIF(size_sqft, 1) > 0.005  -- using NULLIF to avoid returning NULL/attempting invalid division
ORDER BY total_bedroom DESC

-- 11. Which district has the widest price range between the cheapest and most expensive property?

SELECT 
	location,
	MAX(prices) - MIN(prices) price_range
FROM power_bi_import
GROUP BY location
ORDER BY price_range DESC


-- Advanced Analytics: Best Investment Opportunities

-- 12.  Which properties have the best balance of price, size, and number of bedrooms?

SELECT 
	TOP 10 location,
	property_type,
	total_bedroom,
	size_sqft,
	land_status,
	prices,
	ROUND(prices / NULLIF(size_sqft, 0), 2) price_per_sqft,
	ROUND(prices / NULLIF(total_bedroom, 0), 2) price_per_bedroom
FROM power_bi_import
ORDER BY price_per_sqft ASC, price_per_bedroom ASC

-- 13. What are the top 5 most expensive properties by property type?

SELECT * 
FROM (
	SELECT 
		*,
		RANK() OVER(PARTITION BY property_type ORDER BY prices DESC) rank
	FROM power_bi_import
	) ranked_property
WHERE rank <= 5

-- 14. If we divide properties into price quartiles, how many properties fall into each category?


SELECT
	price_quartile,
	COUNT(*) total_properties
FROM (
	SELECT 
		NTILE(4) OVER(ORDER BY prices) price_quartile
	FROM power_bi_import
	) quartile_range
GROUP BY price_quartile
ORDER BY price_quartile