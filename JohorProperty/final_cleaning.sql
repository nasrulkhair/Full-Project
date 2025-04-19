-- Analysis on Johor Property Dataset --

/* SInce the analysis will only be focusing on the 
Landed vs high_rise house, the dataset need to be cleaned
and only have the wanted data only
*/


-- Creating a view table for Power BI import

CREATE VIEW power_bi_import AS
SELECT *
FROM johor_prop
WHERE property_type NOT IN ('shop_lot')

SELECT DISTINCT(property_type)
FROM power_bi_import