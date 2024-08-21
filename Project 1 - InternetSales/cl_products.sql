-- Cleansed DIM_Product table

SELECT
    p.[ProductKey],
    p.[ProductAlternateKey] AS ProductItemCode,
    -- [ProductSubcategoryKey]
    -- [WeightUnitMeasureCode]
    -- [SizeUnitMeasureCode]
    p.[EnglishProductName] AS product_name,
    ps.EnglishProductSubcategoryName AS sub_category,
    pc.EnglishProductCategoryName AS product_category,
    -- [SpanishProductName]
    -- [FrenchProductName]
    -- [StandardCost]
    -- [FinishedGoodsFlag]
    p.[Color] AS product_color,
    -- [SafetyStockLevel]
    -- [ReorderPoint]
    -- [ListPrice]
    p.[Size] AS product_size,
    -- [SizeRange]
    -- [Weight]
    -- [DaysToManufacture]
    p.[ProductLine] AS product_line,
    -- [DealerPrice]
    -- [Class]
    -- [Style]
    p.[ModelName] AS product_model_name,
    -- [LargePhoto]
    p.[EnglishDescription] AS product_description,
    -- [FrenchDescription]
    -- [ChineseDescription]
    -- [ArabicDescription]
    -- [HebrewDescription]
    -- [ThaiDescription]
    -- [GermanDescription]
    -- [JapaneseDescription]
    -- [TurkishDescription]
    -- [StartDate]
    -- [EndDate]
    p.Status AS Example,
    ISNULL(p.Status, 'Outdated') AS product_status
FROM 
    dbo.DimProduct AS p 
LEFT JOIN 
    dbo.DimProductSubcategory AS ps ON ps.ProductSubCategoryKey = p.ProductSubCategoryKey 
LEFT JOIN 
    dbo.DimProductCategory AS pc ON ps.ProductCategoryKey = pc.ProductCategoryKey
ORDER BY
    p.ProductKey ASC;
