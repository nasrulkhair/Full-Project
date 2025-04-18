import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from datetime import datetime
import os

def all_page_url(start_url):
    all_urls = []
    url = start_url

    while url:
        # Send request with a user-agent
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        if response.status_code != 200:
            break

        soup = BeautifulSoup(response.text, "html.parser")

        # Add the current page URL
        all_urls.append(url)

        # Find the next page
        next_link = soup.find(
            "a", {"aria-label": "Next page"}
        )  # Dynamically find the next page
        if next_link and next_link.get("href"):
            next_url = next_link["href"]

            # If the next URL is relative, prepend the base URL
            if next_url.startswith("http"):
                url = next_url
            else:
                url = "https://www.mudah.my" + next_url
        else:
            break  # Stop if no next page found

    return all_urls


def extract_data(url):
    """Extract relevant data fields from each URL"""

    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    if response.status_code != 200:
        print(f"Failed to fetch {url}")
        return None

    soup = BeautifulSoup(response.content, "html.parser")

    data_list = []

    # Find all property listings on the page
    listings = soup.find_all(
        "div", class_="w_100% p_12px_16px d_flex flex-d_column jc_space-between ai_stretch"
    )  # Adjust based on the website's structure

    for listing in listings:
        try:
            type_element = listing.find("p")
            type = type_element.get_text(strip=False) if type_element else "N/A"

            price_element = listing.find("span", class_="currPrice")
            price = price_element.get_text(strip=True) if price_element else "N/A"

            location_element = listing.find("h3", class_="c_black")
            location = (
                location_element.get_text(strip=True) if location_element else "N/A"
            )

            span_elements = listing.find_all(
                "span", class_="fs_sm lh_1.25rem font-style_normal fw_bold c_var(--mudah-colors-text-hi-emp)"
            )
            size = (
                span_elements[0].get_text(strip=True)
                if len(span_elements) > 0
                else "N/A"
            )
            bed = (
                span_elements[1].get_text(strip=True)
                if len(span_elements) > 1
                else "N/A"
            )
            bath = (
                span_elements[2].get_text(strip=False)
                if len(span_elements) > 2
                else "N/A"
            )

            status_elements = listing.find_all("span", class_="c_var(--mudah-colors-text-hi-emp) fs_sm lh_1.25rem font-style_normal fw_normal")
            status = (
                status_elements[3].get_text(strip=True)
                if len(status_elements) > 3
                else "N/A"
            )

            data_list.append(
                {
                    "House Type": type,
                    "Price": price,
                    "Location": location,
                    "Size (sq.ft)": size,
                    "No.of Bed": bed,
                    "No.of Bath": bath,
                    "Land Status": status,
                }
            )

        except AttributeError:
            continue

    return data_list


# Start URL for Johor new properties
start_url = "https://www.mudah.my/johor/new-properties"

# Run scraper
pagination_urls = all_page_url(start_url)

# Scrape data from all pages
all_data = []
for page_url in pagination_urls:
    time.sleep(2)  # To avoid getting blocked by page admin
    extracted_data = extract_data(page_url)
    if extracted_data:
        all_data.extend(extracted_data)

df = pd.DataFrame(all_data)
print(df.head())
print(df.shape)

# Create a unique file name with timestamp to avoid overwriting
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
file_path = f"C:\\Users\\User\\Desktop\\Data Analyst\\End To End Project\\Project 8 - Johor Property\\johor_prop_{timestamp}.csv"

<<<<<<< HEAD
df.to_csv(r"C:\Users\User\Desktop\Data Analyst\End To End Project\Project 8 - Johor Property\johor_prop.csv")

=======
# Check if file is open (optional): You could handle permissions here or add checks to make sure it's not open
if os.path.isfile(file_path):  # Check if the file exists (open or not)
    try:
        df.to_csv(file_path)
        print(f"Data saved to {file_path}")
    except PermissionError as e:
        print(f"Permission error: {e}")
else:
    df.to_csv(file_path)
    print(f"Data saved to {file_path}")
>>>>>>> 02124a2a40efbe33f9f5bc2cf7ac507e7707971d
