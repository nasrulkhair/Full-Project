

'''
ETL Process for Trading Data
This script outlines the ETL (Extract, Transform, Load) process for trading data.
It includes the extraction of data from various sources, transformation of the data to fit the analysis needs, and loading the final datasets for further analysis.
'''

# Required Libraries
import pandas as pd
import numpy as np
import os
from sqlalchemy import create_engine
import pyodbc


# 1. Extract Data From Local Files

engine = create_engine("mssql+pyodbc://@nasrulkhair\SQLEXPRESS/Data Warehouse?driver=ODBC+Driver+17+for+SQL+Server;Trusted_Connection=yes")


# Esok determine the direction of the ETL process. malam ni tidur dulu. kau un blur nak code apa ni