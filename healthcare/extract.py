from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import time

# Set up Chrome driver
service = Service(r"C:\Users\User\Downloads\chromedriver-win64\chromedriver.exe")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

start_url = "https://www.mlperformance.co.uk/collections/engine-oil-recommender?priceMin=1&priceMax=84763&product_type=Product+Type_Engine+Oil"
driver.get(start_url)

# Collect data
product_data = []

while True:
    try: