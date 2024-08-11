-- Cleansing DIM_Customer Table

SELECT 
    c.customerkey AS CustomerKey,
    -- [GeographyKey]
    -- [CustomerAlternateKey]
    -- [Title]
    c.firstname AS First_Name,
    -- [MiddleName]
    c.lastname AS Last_Name,
    c.firstname + ' ' + c.lastname AS Full_Name,
    -- [NameStyle]
    -- [BirthDate]
    -- [MaritalStatus]
    -- [Suffix]
    CASE c.gender 
        WHEN 'M' THEN 'Male' 
        WHEN 'F' THEN 'Female' 
    END AS [Gender],
    -- [EmailAddress]
    -- [YearlyIncome]
    -- [TotalChildren]
    -- [NumberChildrenAtHome]
    -- [EnglishEducation]
    -- [SpanishEducation]
    -- [FrenchEducation]
    -- [EnglishOccupation]
    -- [SpanishOccupation]
    -- [FrenchOccupation]
    -- [HouseOwnerFlag]
    -- [NumberCarsOwned]
    -- [AddressLine1]
    -- [AddressLine2]
    -- [Phone]
    c.datefirstpurchase AS DateFirstPurchase,
    -- [CommuteDistance]
    g.city AS Customer_City
FROM 
    dbo.DimCustomer AS c 
LEFT JOIN 
    dbo.DimGeography AS g ON g.geographykey = c.geographykey
ORDER BY 
    CustomerKey ASC;
