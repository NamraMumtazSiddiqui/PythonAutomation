from selenium import webdriver
from selenium.common.exceptions import UnexpectedTagNameException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time

# Path to your chromedriver executable
driver_path = r"C:\Users\HP\Downloads\Chromedrivers\Drivers\chromedriver.exe"

# Set up the ChromeDriver Service
serviceobj = Service(driver_path)

# Initialize the Chrome WebDriver with the service
driver1 = webdriver.Chrome(service=serviceobj)

# Create a new Chrome browser instance
driver1.get("https://www.google.com")

# Save screenshot with escaped path
driver1.save_screenshot(r"C:\Users\HP\PycharmProjects\Test Automation-786\Screenshots\FirstScreenshot.png")
# Take a full-page screenshot
driver1.get_screenshot_as_file(r"C:\Users\HP\PycharmProjects\Test Automation-786\Screenshots\FullPageScreenshot.png")