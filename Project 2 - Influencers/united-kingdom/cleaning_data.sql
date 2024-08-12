/*

Data Cleaning steps:

1. Remove unnecessary column by selecting the one we need
2. Extract theyoutube channel names from the firts column
3. Rename the column names.

*/
 

SELECT 
	NOMBRE,
	total_subscribers,
	total_views,
	total_videos
FROM 
	dbo.top_uk_youtuber_2024

-- extracting channel name/clean - using CHARINDEX and SUBSTRING function


CREATE VIEW view_uk_youtuber_2024 AS

SELECT 
	CAST(SUBSTRING(NOMBRE, 1, CHARINDEX('@', NOMBRE) -1) AS VARCHAR(100)) AS channel_name,
	total_subscribers,
	total_views,
	total_videos
FROM 
	dbo.top_uk_youtuber_2024



