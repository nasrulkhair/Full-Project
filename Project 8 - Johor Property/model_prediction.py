# House Price Prediction
 
# ==============================================================================
# Data Preparation
# ==============================================================================

import pandas as pd
 
df = pd.read_csv(r"C:\Users\User\Desktop\Data Analyst\End To End Project\Project 8 - Johor Property\transform_johor_prop.csv")
df = df[df["property_type"] != "shop_lot"]
print(df["property_type"].unique())
#print(df.isnull().sum())


# ==============================================================================
# Feature Engineering
# ==============================================================================

from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder

'''
converting category column to category dtype as habit, huge effect if handling
large dataset.
'''

print(df.dtypes)  # land_status/property_type/land_status

# applying ohe for nominal ()
ohe = OneHotEncoder(sparse_output=False, drop="first")  # to avoid multocllinearity

cols = ["location", "property_type", "land_status"]

encoded_location = ohe.fit_transform(df[["location"]])
encoded_cols = ohe.fit_transform(df[cols])
print(encoded_cols.shape)