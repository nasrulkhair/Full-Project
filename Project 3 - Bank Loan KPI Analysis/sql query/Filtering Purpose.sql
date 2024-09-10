
-- Bank Loan Report Overview

SELECT *
FROM bank_loan_data

-- By Month
SELECT
	MONTH(issue_date) AS Month_Number,
	DATENAME(MONTH, issue_date) AS Month_Name,
	COUNT(id) AS Total_Loan_Applications,
	SUM(loan_amount) AS Total_Funded_Amount,
	SUM(total_payment) AS Total_Amount_Received
FROM
	bank_loan_data
GROUP BY
	MONTH(issue_date), DATENAME(MONTH, issue_date)
ORDER BY
	MONTH(issue_date)

-- By State

SELECT 
	address_state AS State, 
	COUNT(id) AS Total_Loan_Applications,
	SUM(loan_amount) AS Total_Funded_Amount,
	SUM(total_payment) AS Total_Amount_Received
FROM 
	bank_loan_data
GROUP BY 
	address_state
ORDER BY 
	address_state

-- By Term

SELECT 
	term AS Term, 
	COUNT(id) AS Total_Loan_Applications,
	SUM(loan_amount) AS Total_Funded_Amount,
	SUM(total_payment) AS Total_Amount_Received
FROM 
	bank_loan_data
GROUP BY 
	term
ORDER BY 
	term

-- BY Employment Length

SELECT 
	emp_length AS Employee_Length, 
	COUNT(id) AS Total_Loan_Applications,
	SUM(loan_amount) AS Total_Funded_Amount,
	SUM(total_payment) AS Total_Amount_Received
FROM 
	bank_loan_data
GROUP BY 
	emp_length
ORDER BY 
	emp_length

-- By Purpose

SELECT 
	purpose AS PURPOSE, 
	COUNT(id) AS Total_Loan_Applications,
	SUM(loan_amount) AS Total_Funded_Amount,
	SUM(total_payment) AS Total_Amount_Received
FROM 
	bank_loan_data
GROUP BY 
	purpose
ORDER BY 
	purpose

-- By Home Ownership

SELECT 
	home_ownership AS Home_Ownership, 
	COUNT(id) AS Total_Loan_Applications,
	SUM(loan_amount) AS Total_Funded_Amount,
	SUM(total_payment) AS Total_Amount_Received
FROM bank_loan_data
GROUP BY home_ownership
ORDER BY home_ownership
