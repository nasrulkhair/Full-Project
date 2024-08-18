SELECT * 
FROM bank_loan_data

-- Total Amount Received
SELECT 
 SUM(total_payment) AS Total_Amount_Received
FROM
	bank_loan_data

-- MTD Total Amount Received
SELECT 
 SUM(total_payment) AS Total_Amount_Received
FROM
	bank_loan_data
WHERE 
	MONTH(issue_date) = 12 AND YEAR(issue_date) = 2021

-- Previous MTD Total AMount Received

SELECT 
 SUM(total_payment) AS Total_Amount_Received
FROM
	bank_loan_data
WHERE 
	MONTH(issue_date) = 11 AND YEAR(issue_date) = 2021