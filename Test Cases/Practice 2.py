from datetime import time
from selenium import webdriver
from selenium.common import UnexpectedTagNameException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webelement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import time

driver_path = r"C:\Users\HP\Downloads\Chromedrivers\Drivers\chromedriver.exe"
serviceobj=Service(driver_path)
driver1=webdriver.Chrome(service=serviceobj)

driver1.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
username=WebDriverWait(driver1,30).until(EC.element_to_be_clickable((By.NAME,"username"))
)
username.send_keys("Admin")
password=WebDriverWait(driver1,30).until(EC.element_to_be_clickable((By.NAME,"password")))
password.send_keys("admin123")
btn=WebDriverWait(driver1, 10).until(
   EC.element_to_be_clickable((By.TAG_NAME, "button")))
btn.click()