# Import required libraries
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv(r"C:\Users\User\Desktop\Data Analyst\End To End Project\Project 8 - Johor Property\transform_johor_prop.csv")

# Hypothesis 1: Does house size significantly impact price? (T-test)

"""
Null Hypothesis (H₀): There is no statistically significant relationship between house size and price.
Alternative Hypothesis (H₁): There is a statistically significant relationship between house size and price.
"""

# Categorize house sizes into "Small" and "Large" for T-test
df["size_category"] = pd.qcut(df["size_sqft"], 2, labels=["Small", "Large"])

# Extract prices for each category
small_prices = df[df["size_category"] == "Small"]["prices"]
large_prices = df[df["size_category"] == "Large"]["prices"]

# Function to perform T-test
def perform_t_test(group1, group2):
    """
    Conducts an independent T-test between two groups.
    
    Parameters:
        group1 (Series): Prices of small houses
        group2 (Series): Prices of large houses

    Returns:
        t_stat (float): T-statistic value
        p_value (float): P-value
    """
    t_stat, p_value = stats.ttest_ind(group1, group2, equal_var=False)
    return t_stat, p_value

# Run T-test
t_stat, p_value = perform_t_test(small_prices, large_prices)

# Display results
print("=" * 50)
print("📊 T-test Results: House Size vs. Price")
print("=" * 50)
print(f"T-statistic: {t_stat:.3f}")
print(f"P-value    : {p_value:.5f}")
print("\nInterpretation:")
if p_value < 0.05:
    print("The result is statistically significant (p < 0.05).")
    print("Reject H₀: House size significantly impacts price.")
else:
    print("The result is NOT statistically significant (p ≥ 0.05).")
    print("Fail to reject H₀: No strong evidence that house size impacts price.")

# ==================================================
# 📊 T-test Results: House Size vs. Price
# ==================================================
# T-statistic: -7.890
# P-value    : 0.00000
#
# Interpretation:
# ✅ The result is statistically significant (p < 0.05).
#    → Reject H₀: House size significantly impacts price.
# ------------------------------


# =================================================================================================================================================================================

# Hypothesis 2: Are house prices different by district?
