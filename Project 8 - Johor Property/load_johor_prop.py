"""-------------------------Load: VSCODE --> MSSQL-----------------------------------"""


from sqlalchemy import create_engine
import pandas as pd


def load_file(csv):
    df = pd.read_csv(csv, index_col=0)
    return df

# Load data

df = load_file(r"C:\Users\User\Desktop\Data Analyst\End To End Project\Project 8 - Johor Property\transform_johor_prop.csv")
#print(df.head())

# Connect to MSSQL

server = "NASRULKHAIR\SQLEXPRESS"
database = "Johor Properties"
try:
    conn_str = f"mssql+pyodbc://@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server&Trusted_Connection=yes"
    engine = create_engine(conn_str)
    # Load into MSSQL
    df.to_sql("johor_prop", con=engine, if_exists="replace", index=False)
    print("Data loaded into MSSQL")
except:
    print("failed to create connection!")

