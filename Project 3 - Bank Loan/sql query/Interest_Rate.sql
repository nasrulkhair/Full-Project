
SELECT *
FROM bank_loan_data


-- Average Interest

SELECT
	ROUND(AVG(int_rate) * 100,2) AS Avg_Int_Rate
FROM
	bank_loan_data

-- MTD Average Interest
SELECT
	ROUND(AVG(int_rate) * 100,2) AS Avg_Int_Rate
FROM
	bank_loan_data
WHERE
	MONTH(issue_date) = 12 

--PMTD Average Interest
SELECT
	ROUND(AVG(int_rate) * 100,2) AS Avg_Int_Rate
FROM
	bank_loan_data
WHERE
	MONTH(issue_date) = 11