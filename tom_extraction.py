from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

# Initialize the WebDriver (ensure the path is correct)
driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

# Open the TomTom Traffic Index ranking page
driver.get("https://www.tomtom.com/traffic-index/ranking/")

# Wait for the page to load the dynamic content
time.sleep(10)  # Adjust sleep time if necessary

# Accept cookies if prompted (adjust the selector as needed)
try:
    accept_cookies_button = driver.find_element(By.ID, "onetrust-accept-btn-handler")
    accept_cookies_button.click()
    time.sleep(2)  # Wait for the acceptance to process
except:
    pass  # If no cookie prompt, continue

# Extract data rows
rows = driver.find_elements(By.CSS_SELECTOR, "table.table tbody tr")

# Prepare lists to store data
data = {
    "World Rank": [],
    "City": [],
    "Avg Travel Time per 6 mi": [],
    "Change from 2023": [],
    "Congestion Level %": [],
    "Time Lost per Year": [],
    "Congestion World Rank": []
}

# Iterate over each row and extract data
for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")
    if len(cells) >= 7:
        data["World Rank"].append(cells[0].text.strip())
        data["City"].append(cells[1].text.strip())
        data["Avg Travel Time per 6 mi"].append(cells[2].text.strip())
        data["Change from 2023"].append(cells[3].text.strip())
        data["Congestion Level %"].append(cells[4].text.strip())
        data["Time Lost per Year"].append(cells[5].text.strip())
        data["Congestion World Rank"].append(cells[6].text.strip())

# Close the WebDriver
driver.quit()

# Create a DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("tomtom_traffic_data.csv", index=False)

print("Data extraction complete. Saved to 'tomtom_traffic_data.csv'.")
