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
        # Wait for the page to load and ensure products are visible
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.custom-collection-grid-section__card"))
        )
        
        # Sleep to ensure the page is fully loaded
        time.sleep(3)
        
        # Find all product elements on the page
        products = driver.find_elements(By.CSS_SELECTOR, "div.custom-collection-grid-section__card")
        print(f"Found {len(products)} products on the current page.")

        # Loop through each product and extract data
        for product in products:
            try:
                name = product.find_element(By.CSS_SELECTOR, "h3.custom-collection-grid-section__title a").text
                
                # Extract brand
                brand = product.find_element(By.CSS_SELECTOR, "p.custom-collection-grid-section__vendor").text
                   
                # Extract price
                try:
                    price_element = product.find_element(By.CSS_SELECTOR, "p.custom-collection-grid-section__price span.custom-collection-grid-section__price--current")
                    price = price_element.text.strip()
                except Exception:
                    price = 'No price available'  # Handle missing price gracefully

                # Append data
                product_data.append({
                    "Name": name,
                    "Brand": brand,
                    "Price": price
                })
                print(f"Scraped product: {name}") # Debug output
                
            except Exception as e:
                print(f"Error extracting product data: {e}")
        
        # Try to find the next button and click it
        next_button = driver.find_element(By.CSS_SELECTOR, "a.pagination-next")
        
        # Check if the "Next" button is disabled (meaning no more pages)
        if "disabled" in next_button.get_attribute("class"):
            print("No more pages to scrape.")
            break
        
        # Scroll the next button into view
        driver.execute_script("arguments[0].scrollIntoView();", next_button)
        
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(next_button)
        )
        
        actions = ActionChains(driver)
        actions.move_to_element(next_button).click().perform()
        
        # Wait for the next page to load (increased sleep time)
        time.sleep(5)  # Adjust the sleep time to ensure the page loads fully
        
    except Exception as e:
        print(f"Error during page navigation or scraping: {e}")
        break

# Save all scraped data to CSV after scraping all pages
if product_data:
    df = pd.DataFrame(product_data)
    df.to_csv('ml_performance_products.csv', index=False)
    print("Scraping completed and data saved to ml_performance_products.csv")
else:
    print("No data was scraped.")
    
driver.quit()
