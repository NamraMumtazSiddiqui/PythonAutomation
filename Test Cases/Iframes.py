import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Path to the chromedriver executable
driver_path = r"C:\Users\HP\Downloads\Chromedrivers\Drivers\chromedriver.exe"
serviceobj = Service(driver_path)

# Initialize WebDriver
driver1 = webdriver.Chrome(service=serviceobj)

# Open the website
driver1.get("https://practice-automation.com/iframes/")

# Locate all iframes and print the count
iframes = driver1.find_elements(By.TAG_NAME, "iframe")
print(f"Total number of iframes: {len(iframes)}")

# Switch to the iframe using its id or name
driver1.switch_to.frame("iframe-1")

# Wait for the 'Get started' button to be clickable
get_started_button = WebDriverWait(driver1, timeout=30).until(
    EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Get started']"))
)

# Scroll the element into view using JavaScript
driver1.execute_script("arguments[0].scrollIntoView(true);", get_started_button)

# Pause for a moment to ensure the scroll completes
time.sleep(1)

# Click the button
get_started_button.click()

# Pause for 5 seconds to observe the action
time.sleep(5)

# Close the browser
driver1.quit()
