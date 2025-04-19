
import pandas as pd
import scipy.stats as stats

df = pd.read_csv(r"C:\Users\User\Desktop\Data Analyst\End To End Project\johorProperty\transform_johor_prop.csv")
df = df[df["property_type"].isin(["landed", "high_rise"])]
#print(df.head())
#print(df["property_type"].unique())


# ===========================================================================================================================

# Hypothesis Definition:
#   -> Ho: There is no significant difference in prices between landed and high-rise properties
#   -> H1: Landed properties have significantly different prices compared to high-rise properties

# Running the A/B testing

group_A = df[df["property_type"]=="landed"]["prices"]
group_B = df[df["property_type"]=="high_rise"]["prices"]


#   Check for Normality
# Shapiro-Wilk Test (if p-value < 0.05, data is NOT normal)

shapiro_A = stats.shapiro(group_A)
shapiro_B = stats.shapiro(group_B)
print(shapiro_A, shapiro_B)

if shapiro_A.pvalue > 0.05 and shapiro_B.pvalue > 0.05:
    t_stats, p_value = stats.ttest_ind(group_A, group_B)
    print(f"T-test: tstat = {tstats:.3f}, p-value = {p_value:.5f}")
else:
    u_stats, p_value = stats.mannwhitneyu(group_A, group_B, alternative = "two-sided")
    print(f"MWU-test: ustat = {u_stats:.3f}, p-value = {p_value:.5f}")
    

# --- Interpretation ---
if p_value < 0.05:
    print("✅ Significant difference found: Property type affects house prices!")
else:
    print("❌ No significant difference: Property type does NOT affect house prices.")