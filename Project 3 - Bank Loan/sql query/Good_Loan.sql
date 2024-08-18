SELECT * 
FROM bank_loan_data

-- Good Loan Percentage (%)
-- to check the unique values inside the loan_status column
SELECT 
	DISTINCT(loan_status)
FROM 
	bank_loan_data

SELECT
	CAST(ROUND((COUNT(CASE WHEN loan_status = 'Fully Paid' OR loan_status = 'Current' THEN id END) * 100.0) /
	COUNT(id),2) AS DECIMAL(10,2)) AS Good_Loan_Percentage
FROM 
	bank_loan_data

-- Good Loan Application

SELECT
	COUNT(id) AS Good_Loan_Application
FROM 
	bank_loan_data
WHERE
	loan_status = 'Fully Paid' OR loan_status = 'Current'

-- Good Loan Funded Amount

SELECT 
	SUM(loan_amount) AS Good_Loan_Funded_Amount
FROM
	bank_loan_data
WHERE
	loan_status = 'Fully Paid' OR loan_status = 'Current'


-- Good Loan Amount Received

SELECT
	SUM(total_payment) AS Good_Loan_Amount_Received
FROM 
	bank_loan_data
WHERE
	loan_status = 'Fully Paid' OR loan_status = 'Current'