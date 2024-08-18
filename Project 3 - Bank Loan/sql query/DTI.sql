SELECT * 
FROM bank_loan_data

-- Average Debt to Income Ratio

SELECT 
	AVG(dti) * 100 AS Avg_DTI
FROM 
	bank_loan_data

-- MTD Average DTI ratio

SELECT 
	AVG(dti) * 100 AS Avg_DTI
FROM 
	bank_loan_data
WHERE
	MONTH(issue_date) = 12

-- PMTD Avergae DTI ratio
SELECT 
	AVG(dti) * 100 AS Avg_DTI
FROM 
	bank_loan_data
WHERE
	MONTH(issue_date) = 11