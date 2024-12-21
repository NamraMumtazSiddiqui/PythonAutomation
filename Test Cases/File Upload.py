import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
import pytest
# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument('--start-maximized')

# Initialize WebDriver
driver = r"C:\Users\HP\Downloads\Chromedrivers\Drivers\chromedriver.exe"
serviceobj = Service(driver)
driver1 = webdriver.Chrome(service=serviceobj,options=chrome_options)

# Navigate to the URL with the file upload form
driver1.get("https://easyupload.io/")


# Locate the file input element
file_locator=driver1.find_element(By.XPATH,"//body/main[1]/div[1]/div[1]/div[3]/form[1]/div[2]/button[1]")
file_locator.click()
# Specify the file path to be uploaded
file_path = r'C:\Users\HP\PycharmProjects\Test Automation-786\Test Cases\beziercurve-200402173426.pptx'

# Upload the file by sending the file path to the file input element
file_locator.send_keys(file_path)
time.sleep(20)

