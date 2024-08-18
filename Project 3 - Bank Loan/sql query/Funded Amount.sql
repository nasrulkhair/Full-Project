-- to cehck all columns data
SELECT *
FROM bank_loan_data

-- Finding total funded amount
-- Total Funded Amount
SELECT SUM(loan_amount) AS Total_Funded_Amount
FROM bank_loan_data

-- MTD Total Funded Amount
SELECT 
	SUM(loan_amount) AS MTD_Total_Funded_Amount
FROM 
	bank_loan_data
WHERE
	MONTH(issue_date) = 12 AND YEAR(issue_date) = 2021

-- Previous MTD Total Funded Amount

SELECT 
	SUM(loan_amount) AS MTD_Total_Funded_Amount
FROM 
	bank_loan_data
WHERE
	MONTH(issue_date) = 11 AND YEAR(issue_date) = 2021