#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
from datetime import datetime
import re
import os
#import nb_black

# read the latest file 

directory = "C:\\Users\\User\\Desktop\\Data Analyst\\End To End Project\\johorProperty"

# pattern to search
pattern = r"johor_prop_(\d{8})\.csv"

files = [f for f in os.listdir(directory) if re.match(pattern, f)]
latest_file = max(files, key=lambda x: datetime.strptime(re.search(pattern, x).group(1), "%Y%m%d"))
latest_file_path = os.path.join(directory, latest_file)

johor = pd.read_csv(latest_file_path)
johor.head()

# show full row
pd.options.display.max_columns = None


# In[15]:


# remove unwanted column

johor = johor[['House Type', 'Price', 'Location', 'Size (sq.ft)',
       'No.of Bed', 'No.of Bath', 'Land Status']]
print(johor.head())
print(johor.shape)


# In[16]:


# renaming columns name for standardization

johor.rename(columns= {
    'House Type': 'property_type',
    'Price': 'price', 
    'Location': 'location', 
    'Size (sq.ft)': 'size_sqft', 
    'No.of Bed': 'total_bedroom',
    'No.of Bath': 'total_bathroom', 
    'Land Status': 'land_status'
}, inplace = True)

johor.columns


# In[17]:


# cleaning each column before proceed to Statistical Analysis

# 1. property_type

johor["property_type"].head()

house_types = []

regex_property = r"(?<=New\s)(\S+)"


for house in johor["property_type"]:
    house_matches = re.search(regex_property, house)
    if house_matches is not None:
        house_type = house_matches.group(0).strip()
    else:
        house_type = ""
    house_types.append(house_type)
    
#print(house_types)

johor["property_type_extract"] = house_types
print(johor.head())


# In[18]:


# 2. price

johor["prices"] = johor["price"].str.split(expand=True)[1].str.replace(",","")
johor["prices"] = johor["prices"].astype("int")
johor["prices"].dtype


# In[19]:


# 3. location - since all properties in the dataset are from Johor, so we wil focus on the district only

# lower case each letter
johor["location"] = [x.lower() for x in johor["location"]]
# Check for no. of district under Johor < suppose total under 
#print(johor["location"].value_counts())  # total 58

# check the value of the unknown district
#print(johor["location"].nunique())

# Handling inconsistent lcoation names

# info from google - Batu Pahat, Johor Bahru, Kluang, Kota Tinggi, Mersing, Muar, Pontian, and Segamat (8 district)

valid_districts = {
    "batu pahat": "batu pahat",
    "johor bahru": "johor bahru",
    "kluang": "kluang",
    "kota tinggi": "kota tinggi",
    "mersing": "mersing",
    "muar": "muar",
    "pontian": "pontian",
    "segamat": "segamat"
}

town_to_district = {
    "johor bahru": "johor bahru",
    "kulai": "kulai",
    "kluang": "kluang",
    "pasir gudang": "johor bahru",
    "senai": "kulai",
    "skudai": "johor bahru",
    "iskandar puteri": "johor bahru",
    "permas jaya": "johor bahru",
    "masai": "johor bahru",
    "muar": "johor",
    "gelang patah": "johor bahru",
    "parkland by the river": "johor bahru",
    "tebrau": "johor bahru",
    "sentrio residences @ senai": "kulai",
    "horizon hills": "johor bahru",
    "kota tinggi": "kota tinggi",
    "pangsapuri ksl bukit gemilang": "johor bahru",
    "tangkak": "muar",
    "ayer hitam": "kluang",
    "d' secret garden": "johor bahru",
    "pengerang": "kota tinggi",
    "bandar baru permas jaya": "johor bahru",
    "parc regency": "johor bahru",
    "ksl residence 2 @ kangkar tebrau": "johor bahru",
    "veranda residence": "johor bahru",
    "setia indah": "johor bahru",
    "d'secret garden @ kempas indah": "johor bahru",
    "verte medini condominium": "johor bahru",
    "desaru utama residence": "kota tinggi",
    "the senai garden": "kulai",
    "batu pahat": "batu pahat",
    "pontian": "pontian",
    "pandan residence": "johor bahru",
    "bakri": "muar",
    "mersing": "mersing",
    "sierra heights (residensi siera perdana)": "johor bahru",
    "yong peng": "kluang",
    "puteri harbour": "johor bahru",
    "santai @ eco spring": "johor bahru",
    "mutiara austin": "johor bahru",
    "east bay (seri bayan)": "johor bahru",
    "the garden residences": "johor bahru",
    "senibong": "johor bahru",
    "m minori": "johor bahru",
    "d'summit residences": "johor bahru",
    "seri austin residence luxury apartment": "johor bahru",
    "marina cove": "johor bahru",
    "setia tropika": "johor bahru",
    "permas sentral": "johor bahru",
    "idaman residence @ nusa idaman": "johor bahru",
    "tampoi height serviced apartment": "johor bahru",
    "iskandar residences medini": "johor bahru",
    "vista tiara @ mbw bay": "johor bahru",
    "arc @ austin hills": "johor bahru",
    "ksl residences @ daya": "johor bahru",
    "aliva @ mount austin": "johor bahru",
    "kings bay @ country garden danga bay": "johor bahru",
    "ulu tiram": "johor bahru"
}

# function to get the correct district

def get_district(location):
    parts = location.split(",")
    for part in parts:
        part = part.strip()
        if part in valid_districts:
            return valid_districts[part]
        elif part in town_to_district:
            return town_to_district[part]
    else:
        return "Unknown"
        
johor["district"] = johor["location"].apply(get_district)
print(johor["district"].value_counts())


# In[20]:


johor.head()


# In[21]:


# size_sqft

johor["size_sqft"] = johor["size_sqft"].str.replace(",", "").astype("int")
johor["size_sqft"].dtype



# In[22]:


# property_type_extract

valid_property_type = {
    "landed": "landed",
    "high_rise": "high_rise",
    "shop_lot": "shop_lot",
    "factory": "factory"
}

property_type = {
    "Service": "high_rise",
    "2-storey": "landed",
    "1-storey": "landed",
    "Apartment": "high_rise",
    "Terraced": "landed",
    "Semi-Detached": "landed",
    "Condominium": "high_rise",
    "Cluster": "landed",
    "Shop": "shop_lot",
    "Others": "shop_lot",
    "Warehouse": "factory",
    "Bungalow": "landed",
    "3-storey": "high_rise",
    "2.5-storey": "high_rise",
    "Office": "shop_lot",
    "Flat": "high_rise"
}

def get_type(property_name):
    return property_type.get(property_name, "Unknown")

johor["property_type_extract"] = johor["property_type_extract"].apply(get_type)
johor["property_type_extract"].value_counts()


# In[23]:


# remove unwanted columns
johor = johor[["district", "property_type_extract", "size_sqft", "total_bedroom", "total_bathroom", "land_status", "prices"]]
johor.rename(columns={
    "property_type_extract": "property_type",
    "district": "location"}, inplace=True)
johor.head()


# In[24]:


# Handling duplicated values

johor = johor.drop_duplicates()
johor.duplicated().sum()


# In[25]:


# Handling null values


johor.dropna(subset=["total_bedroom", "total_bathroom", "land_status"], inplace=True)
johor = johor.reset_index(drop=True)
print(johor.isna().sum())


# In[ ]:


johor.to_csv(r"C:\Users\User\Desktop\Data Analyst\End To End Project\johorProperty\transform_johor_prop.csv", index=False)


# In[ ]:





# In[ ]:




