# Import required libraries
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv(r"C:\Users\User\Desktop\Data Analyst\End To End Project\JohorProperty\transform_johor_prop.csv")

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
    t_stat, p_value_tt = stats.ttest_ind(group1, group2, equal_var=False)
    return t_stat, p_value_tt

# Run T-test
t_stat, tt_p_value = perform_t_test(small_prices, large_prices)

# Display results
print("=" * 50)
print("📊 T-test Results: House Size vs. Price")
print("=" * 50)
print(f"T-statistic: {t_stat:.3f}")
print(f"P-value    : {tt_p_value:.5f}")
print("\nInterpretation:")
if tt_p_value < 0.05:
    print("The result is statistically significant (p < 0.05).")
    print("Reject H₀: House size significantly impacts price.")
else:
    print("The result is NOT statistically significant (p ≥ 0.05).")
    print("Fail to reject H₀: No strong evidence that house size impacts prices.")

print("\n")

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

# Hypothesis 2: Are house prices different by location?

"""
Null Hypothesis (H₀): There is no significant difference in house prices across different locations.
Alternative Hypothesis (H₁): At least one location has a significantly different mean house price compared to others.
"""

anova_p_value = stats.f_oneway(*(df[df["location"] == d]["prices"] for d in df["location"].unique()))
print(f"Anova test for Location Prices: p-value = {anova_p_value.pvalue:.5f}")

# Display results
print("=" * 50)
print("📊 T-test Results: Location vs. Price")
print("=" * 50)
print(f"P-value    : {anova_p_value.pvalue:.5f}")
print("\nInterpretation:")
if anova_p_value.pvalue < 0.05:
    print("The result is statistically significant (p < 0.05).")
    print("Reject H₀: Location significantly impacts price.")
else:
    print("The result is NOT statistically significant (p ≥ 0.05).")
    print("Fail to reject H₀: No strong evidence that Location impacts price.")
    
print("\n")

# ==================================================
# 📊 Anova Test Results: Location vs. Price
# ==================================================
# P-value    :  0.06862
#
# Interpretation:
# ✅ The result is there is not enough statistical evidence (p > 0.05).
#    → Fail to Reject H₀: House size not significantly impacts price.
#    → However, the p-value is close to 0.05, suggesting a weak indication of possible differences. 
#      A larger sample size or a lower significance threshold (e.g., 0.10) might reveal more insight.
# ------------------------------

# =================================================================================================================================================================================

# Hypothesis 3: Do Freehold and Leasehold properties have different prices?

"""
Null Hypothesis (H₀): There is no significant difference in house prices between Freehold and Leasehold properties.
Alternative Hypothesis (H₁): There is a significant difference in house prices between Freehold and Leasehold properties
"""
freehold_prices = df[df["land_status"]=="Freehold"]["prices"]
leasehold_prices = df[df["land_status"]=="Leasehold"]["prices"]

t_stat_ld, tt_p_value_ld = stats.ttest_ind(freehold_prices, leasehold_prices, equal_var=False)

# Display results
print("=" * 50)
print("📊 T-test Results: Land Status vs. Price")
print("=" * 50)
print(f"T-statistic: {t_stat_ld:.3f}")
print(f"P-value    : {tt_p_value_ld:.5f}")
print("\nInterpretation:")
if tt_p_value_ld < 0.05:
    print("The result is statistically significant (p < 0.05).")
    print("Reject H₀: There is strong statistical evidence that house prices differ significantly between Freehold and Leasehold properties.")
else:
    print("The result is NOT statistically significant (p ≥ 0.05).")
    print("Fail to reject H₀: No strong evidence that Freehold and Leasehold properties impacts prices.")

print("\n")

# ==================================================
# 📊 T-test Results: Freehold and Leasehold properties vs. Price
# ==================================================
# T-statistic: 3.306
# P-value    : 0.00124
#
# Interpretation:
# ✅ The result is statistically significant (p < 0.05).
#    → Reject H₀: Freehold and Leasehold properties significantly impacts price.
#    → The positive T-statistic (3.306) suggests that one group (likely Freehold) has a higher mean price than the other (Leasehold)
# ------------------------------

# =================================================================================================================================================================================

# Correlation Analysis:

correlation_matrix = df[["prices", "size_sqft", "total_bedroom", "total_bathroom"]].corr(method="pearson")
print(f"The Pearson Correlation Matrix: \n: {correlation_matrix}")

plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()