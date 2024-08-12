/*

Testing data:

1. The data needs to be 100 records Youtube Channel (row count test)
2. The data need 4 fields (column test)
3. The channel column must be string format and the other column must be numeric data type (data types check).
4. Each record must be unique in the dataset (duplicate count check).

Row count - 100
column count - 4
Data types
- channel name = varchar
- total_subscribers = int
- total_views = int
- total_videos = int

duplicate_count = 0
*/


-- 1. row count test

SELECT 
	COUNT(*) 
FROM 
	view_uk_youtuber_2024;


-- 2. column count - using information schema

SELECT COUNT(*) AS columns_count 
FROM 
	INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'view_uk_youtuber_2024'


-- 3. Data types check

SELECT COLUMN_NAME, DATA_TYPE
FROM
	INFORMATION_SCHEMA.COLUMNS
WHERE 
	TABLE_NAME = 'view_uk_youtuber_2024';


-- 4. Duplicate Test

SELECT 
	channel_name,
	COUNT(*) AS duplicate_count
FROM 
	view_uk_youtuber_2024
GROUP BY 
	channel_name
HAVING 
	COUNT(*) > 1

-- TEST PASS!! COMPLETED (4/4)


SELECT *
FROM 
	view_uk_youtuber_2024