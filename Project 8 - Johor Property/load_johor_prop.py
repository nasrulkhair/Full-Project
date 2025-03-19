"""-------------------------Load: VSCODE --> MSSQL-----------------------------------"""



from sqlalchemy import create_engine
import pandas as pd


def load_file(csv):
    csv_file = csv
    df = pd.read_csv(csv_file)
    return df

load_file("C:\Users\User\Desktop\Data Analyst\End To End Project\Project 8 - Johor Property\Transform - Johor_prop.csv")