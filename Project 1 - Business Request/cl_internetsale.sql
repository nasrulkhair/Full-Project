-- Cleansed FACT_InternetSale Table

SELECT 
    [ProductKey],
    [OrderDateKey],
    [DueDateKey],
    [ShipDateKey],
    [CustomerKey],
    -- [PromotionKey]
    -- [CurrencyKey]
    -- [SalesTerritoryKey]
    [SalesOrderNumber],
    -- [SalesOrderLineNumber]
    -- [RevisionNumber]
    -- [OrderQuantity]
    -- [UnitPrice]
    -- [ExtendedAmount]
    -- [UnitPriceDiscountPct]
    -- [DiscountAmount]
    -- [ProductStandardCost]
    -- [TotalProductCost]
    [SalesAmount]
    -- [TaxAmt]
    -- [Freight]
    -- [CarrierTrackingNumber]
    -- [CustomerPONumber]
    -- [OrderDate]
    -- [DueDate]
    -- [ShipDate]
FROM 
    dbo.FactInternetSales
WHERE 
    LEFT(OrderDateKey, 4) >= YEAR(GETDATE()) - 2  -- Ensure we only bring two years of data from extraction (e.g., OrderDateKey starting with 2021 and onwards)
ORDER BY
    OrderDateKey ASC;
