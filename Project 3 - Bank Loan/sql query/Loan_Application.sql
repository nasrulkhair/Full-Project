-- checking the imported file and read in overall the data
SELECT 
	* 
FROM 
	bank_loan_data


-- Answering Probelm statement

-- Finding the total loan applications
-- Total Loan Applications
SELECT 
	COUNT(id) AS Total_Loan_Applications
FROM
	bank_loan_data

-- MTD loan applications
SELECT 
	COUNT(id) AS MTD_Total_Loan_Applications
FROM 
	bank_loan_data
WHERE 
	MONTH(issue_date) = 12 AND YEAR(issue_date) = 2021

-- Previous MTD Loan Application
SELECT COUNT(id) AS MTD_Total_Loan_Applications
FROM bank_loan_data
WHERE MONTH(issue_date) = 11 AND YEAR(issue_date) = 2021

