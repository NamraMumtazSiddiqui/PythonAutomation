import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Path to the chromedriver executable
driver_path = r"C:\Users\HP\Downloads\Chromedrivers\Drivers\chromedriver.exe"
serviceobj = Service(driver_path)

# Initialize WebDriver
driver1 = webdriver.Chrome(service=serviceobj)

# Open the website
driver1.get("https://practice-automation.com")
links = driver1.find_elements(By.TAG_NAME, "a")
broken_links = []

for link in links:
    url = link.get_attribute("href")

    if url and (url.startswith("http") or url.startswith("https")):
        try:
            response = requests.head(url, allow_redirects=True)
            if response.status_code >= 400:
                print(f"Broken link: {url} (Status Code: {response.status_code})")
                broken_links.append(url)
            else:
                print(f"Valid link: {url} (Status Code: {response.status_code})")

        except requests.exceptions.RequestException as e:
            print(f"Error checking link: {url} - {e}")
            broken_links.append(url)

print(f"\nTotal broken links found: {len(broken_links)}")
for broken_link in broken_links:
    print(broken_link)

driver1.quit()
