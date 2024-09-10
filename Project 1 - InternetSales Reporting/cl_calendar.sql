-- Cleansing DIM_Date Table

SELECT 
    [DateKey],
    [FullDateAlternateKey] AS Date,
    [EnglishDayNameOfWeek] AS Day,
    -- [DayNumberOfWeek]
    -- [SpanishDayNameOfWeek]
    -- [FrenchDayNameOfWeek]
    -- [DayNumberOfMonth]
    -- [DayNumberOfYear]
    [WeekNumberOfYear] AS WeekNr,
    [EnglishMonthName] AS Month,
    Left([EnglishMonthName], 3) AS MonthShort,  -- Extracting the first three letters for better visualization
    -- [SpanishMonthName]
    -- [FrenchMonthName]
    [MonthNumberOfYear] AS MonthNo,
    [CalendarQuarter] AS Quarter,
    [CalendarYear] AS Year
    -- [CalendarSemester]
    -- [FiscalQuarter]
    -- [FiscalYear]
    -- [FiscalSemester]
FROM 
    dbo.DimDate
WHERE 
    CalendarYear >= 2019;
