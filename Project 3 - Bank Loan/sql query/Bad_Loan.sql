SELECT *
FROM bank_loan_data

-- Bad Loan Percentage (%)

-- checking unqiue values in loan_status column
SELECT 
	DISTINCT(loan_status) AS type_of_status
FROM
	bank_loan_data

SELECT
	CAST(ROUND((COUNT(CASE WHEN loan_status = 'Charged Off' THEN id END) * 100.0) / 
	COUNT(id), 2) AS DECIMAL (10,2)) AS Bad_Loan_Percentage
FROM
	bank_loan_data

-- Bad Loan Application

SELECT 
	COUNT(loan_status) AS Bad_Loan_Application 
 FROM
	bank_loan_data
WHERE
	loan_status = 'Charged Off'

-- Bad Loan Funded Amount

SELECT
	SUM(loan_amount) AS Bad_Loan_Funded_Amount
FROM
	bank_loan_data
WHERE
	loan_status = 'Charged Off'

-- Bad Loan Amount Received

SELECT
	SUM(total_payment) AS Bad_Loan_Amount_Received
FROM
	bank_loan_data
WHERE
	loan_status = 'Charged Off'