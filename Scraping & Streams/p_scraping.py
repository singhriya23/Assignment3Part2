from playwright.sync_api import sync_playwright
import json
import time

# Function to extract traffic data
def scrape_tomtom():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Set False to see the browser
        page = browser.new_page()

        # Attach a listener to print all API requests (for debugging)
        def log_responses(response):
            print(f"🔍 API Request URL: {response.url} | Status: {response.status} | Content-Type: {response.headers.get('content-type', '')}")

        page.on("response", log_responses)

        # Open TomTom Traffic Index page
        page.goto("https://www.tomtom.com/traffic-index/ranking/", timeout=60000)

        print("⏳ Waiting for API response...")

        # Try multiple variations to capture the right API response
        try:
            with page.expect_response(lambda response: "traffic-index" in response.url and response.status == 200 and "json" in response.headers.get("content-type", ""), timeout=60000) as response_info:
                response = response_info.value  # Extract response

            json_data = response.json()
            print(f"✅ API Response Captured with keys: {json_data.keys()}")  # Debugging step

            # Save JSON Data
            with open("tomtom_traffic_data_1.json", "w", encoding="utf-8") as json_file:
                json.dump(json_data, json_file, indent=4)
            print(f"✅ JSON data saved successfully!")

        except Exception as e:
            print(f"❌ Failed to fetch API response: {e}")

        browser.close()

# Run the scraper
scrape_tomtom()
