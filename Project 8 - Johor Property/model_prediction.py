# House Price Prediction
 
# ==============================================================================
# Data Preparation
# ==============================================================================

import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.feature_selection import SelectFromModel
from sklearn.model_selection import RandomizedSearchCV
 
df = pd.read_csv(r"C:\Users\User\Desktop\Data Analyst\End To End Project\Project 8 - Johor Property\transform_johor_prop.csv")
df = df[df["property_type"] != "shop_lot"]
#print(df["property_type"].unique())
#print(df.isnull().sum())


# ==============================================================================
# Feature Engineering
# ==============================================================================

'''
converting category column to category dtype as habit, huge effect if handling
large dataset.
'''

#print(df.dtypes)  # land_status/property_type/land_status

# applying ohe for nominal ()
ohe = OneHotEncoder(sparse_output=False, drop="first")  # to avoid multocllinearity

cols = ["location", "property_type", "land_status"]

encoded_location = ohe.fit_transform(df[["location"]])
encoded_cols = ohe.fit_transform(df[cols])
#print(encoded_cols.shape)

encoded_df = pd.DataFrame(encoded_cols, columns=ohe.get_feature_names_out(cols))
#print(encoded_df.head())

df = pd.concat([df, encoded_df], axis=1)
df.drop(columns = ["location", "property_type", "land_status"], inplace=True)  # drop unwanted columns after encoding
print(df.head(1))

# ==============================================================================
# Train-Val-Test Split
# ==============================================================================

X = df.drop(columns="prices")
y = df["prices"]

X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state = 7)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=7)
print(X_train.shape, y_train.shape, X_val.shape, y_val.shape, X_test.shape, y_val.shape)


# ==============================================================================
# Model Pipeline
# ==============================================================================

lr_pipeline = Pipeline([
    ("model": LinearRegression()),
    ("scaler"): StandardScaler()
])

rf_pipeline = Pipeline([
    ("model": RandomForestRegressor())
])