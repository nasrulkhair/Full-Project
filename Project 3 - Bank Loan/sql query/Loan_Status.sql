SELECT *
FROM bank_loan_data

-- LOAN STATUS

SELECT
	loan_status,
	COUNT(id) AS Loan_Count,
	SUM(total_payment) AS Total_Payment_Received,
	SUM(loan_amount) AS Total_Funded_Amount,
	AVG(int_rate * 100) AS Interest_Rate,
    AVG(dti * 100) AS DTI
FROM 
	bank_loan_data
GROUP BY
	loan_status


-- Amount to Be Received

SELECT
	loan_status,
	SUM(total_payment) AS MTD_Total_Amount_Received, 
	SUM(loan_amount) AS MTD_Total_Funded_Amount
	
FROM
	bank_loan_data
GROUP BY
	loan_status
