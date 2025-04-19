# ==============================================================================  
# House Price Prediction  
# ==============================================================================  

# Importing Required Libraries  
import pandas as pd  
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import OneHotEncoder, StandardScaler  
from sklearn.impute import SimpleImputer  
from sklearn.model_selection import train_test_split, RandomizedSearchCV  
from sklearn.pipeline import Pipeline  
from sklearn.linear_model import LinearRegression, Lasso  
from sklearn.ensemble import RandomForestRegressor  
from xgboost import XGBRegressor  
from sklearn.feature_selection import SelectFromModel  
from scipy.stats import randint  
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# ==============================================================================  
# Data Preparation  
# ==============================================================================  

df = pd.read_csv(r"C:\Users\User\Desktop\Data Analyst\End To End Project\Project 8 - Johor Property\transform_johor_prop.csv")  

# Removing 'shop_lot' property type  
df = df[df["property_type"] != "shop_lot"]  


# ==============================================================================  
# Feature Engineering  
# ==============================================================================  

# One-Hot Encoding for categorical features  
ohe = OneHotEncoder(sparse_output=False, drop="first")  
cols = ["location", "property_type", "land_status"]  
encoded_cols = ohe.fit_transform(df[cols])  
encoded_df = pd.DataFrame(encoded_cols, columns=ohe.get_feature_names_out(cols))  

# Concatenating encoded columns and dropping original categorical columns  
df = pd.concat([df, encoded_df], axis=1)  
df.drop(columns=cols, inplace=True)  

# ==============================================================================  
# Train-Val-Test Split  
# ==============================================================================  

X = df.drop(columns=["prices"])  
y = df["prices"]  

X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=7)  
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=7)  

# Handling missing values using median imputation  
imputer = SimpleImputer(strategy="median")  
X_train = pd.DataFrame(imputer.fit_transform(X_train), columns=X.columns)  
X_val = pd.DataFrame(imputer.transform(X_val), columns=X.columns)  
X_test = pd.DataFrame(imputer.transform(X_test), columns=X.columns)  

#print(y_train.isna().sum())
y_train = y_train.fillna(y_train.median())

# ==============================================================================  
# Model Pipelines  
# ==============================================================================  

# Feature selection using Lasso  
feature_selection = SelectFromModel(Lasso(alpha=0.001))  

# Pipeline for Linear Regression  
lr_pipeline = Pipeline([  
    ("scaler", StandardScaler()),  
    ("feature_selection", feature_selection),  
    ("model", LinearRegression())  
])  

# Pipeline for Random Forest  
rf_pipeline = Pipeline([  
    ("feature_selection", feature_selection),  
    ("model", RandomForestRegressor(random_state=7))  
])  

# Parameter grid for RandomizedSearchCV (Random Forest)  
rf_param_grid = {  
    "model__n_estimators": randint(50, 200),  
    "model__max_depth": randint(3, 20),  
    "model__min_samples_split": randint(2, 10),  
    "model__min_samples_leaf": randint(1, 5)  
}  

rf_random_search = RandomizedSearchCV(rf_pipeline, param_distributions=rf_param_grid, n_iter=10, cv=5, n_jobs=1, random_state=7)  
rf_random_search.fit(X_train, y_train)  
print(f"Best Random Forest Parameters: {rf_random_search.best_params_}")  

# Pipeline for XGBoost  
xgb_pipeline = Pipeline([  
    ("feature_selection", feature_selection),  
    ("model", XGBRegressor(random_state=7))  
])  

# Parameter grid for XGBoost  
xgb_param_grid = {  
    "model__n_estimators": randint(50, 200),  
    "model__max_depth": randint(3, 10),  
    "model__learning_rate": [0.01, 0.05, 0.1, 0.2],  
    "model__subsample": [0.6, 0.8, 1.0]  
}  

xgb_random_search = RandomizedSearchCV(xgb_pipeline, param_distributions=xgb_param_grid, n_iter=10, cv=5, n_jobs=1, random_state=7)  
xgb_random_search.fit(X_train, y_train)  
print(f"Best XGBoost Parameters: {xgb_random_search.best_params_}")  


# ==============================================================================  
# making Predictions  
# ============================================================================== 

# lr
best_lr_model = lr_pipeline.fit(X_train, y_train)
lr_val_preds = best_lr_model.predict(X_val)

feature_importance = pd.Series(best_lr_model.named_steps["model"].coef_, index=X_train.columns)
feature_importance.sort_values().plot(kind="barh", figsize=(8, 5))
plt.title("Feature Importance in Property Price Prediction")
plt.show()

# rf
best_rf_model = rf_random_search.best_estimator_
rf_val_preds = best_rf_model.predict(X_val)

# xgb
best_xgb_model = xgb_random_search.best_estimator_
xgb_val_preds = best_xgb_model.predict(X_val)


# ==============================================================================  
# Model Evaluation  
# ============================================================================== 

def evaluate_model(y_true, y_pred, model_name):
    mae = mean_absolute_error(y_true, y_pred)
    mse = mean_squared_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    
    print(f"model_name: {model_name}")
    print(f"    - Mean Absolute Error: {mae}")
    print(f"    - Mean Squared Error: {mse}")
    print(f"    - R2 Score: {r2}")

Linear_regression_validation =evaluate_model(y_val, lr_val_preds, "Linear Regression (Validation)")
XGBoost_validation = evaluate_model(y_val, xgb_val_preds, "XGBoost (Validation)")
evaluate_model(y_val, rf_val_preds, "Random Forest (Validation)")



# ==============================================================================  
# making predictions on test set  
# ==============================================================================

#sample_data = X_test.iloc[:5]
predictions = best_rf_model.predict(X_test)
#print(predictions)

# ==============================================================================  
# Prediction and Real Comparison 
# ==============================================================================

predicted_sample_df = pd.DataFrame({
    "Predicted Prices": predictions,
    "Real Prices": y_test
})
predicted_sample_df["difference"] = predicted_sample_df["Predicted Prices"] - predicted_sample_df["Real Prices"]
print(predicted_sample_df.head())

# ==============================================================================
plt.figure(figsize=(8, 6))
sns.scatterplot(x=y_test.index, y=y_test, color="red", marker="o", label="Actual Prices")
sns.scatterplot(x=y_test.index, y=predictions, color="blue", marker="x", label="Predicted Prices")
plt.xlabel("Index of Sample")
plt.ylabel("Property Prices")
plt.title("Actual vs. Predicted Property Prices")

# Format y-axis to show in thousands
from matplotlib.ticker import FuncFormatter
formatter = FuncFormatter(lambda x, _: f'{int(x/1000)}K')  # Convert values to K 
plt.gca().yaxis.set_major_formatter(formatter)
plt.legend()
plt.show()
