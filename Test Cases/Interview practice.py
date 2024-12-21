from datetime import time
from tkinter.tix import Select

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver_path = r"C:\Users\HP\Downloads\Chromedrivers\Drivers\chromedriver.exe"

serviceobj=Service(driver_path)
chromedriver=webdriver.Chrome(service=serviceobj)
chromedriver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

#The Page Object Model (POM) is a design pattern in Selenium that helps organize your code
# by creating separate classes for each web page of the application. This makes your tests
# easier to manage and maintain

# How do you wait until the number of results displayed on the page is greater than 0?

#Wait until the number of results is greater than 0
#wait = WebDriverWait(chromedriver, 10)  # 10 seconds timeout
#results = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.orangehrm-login-layout div.orangehrm-login-layout-blob div.orangehrm-login-container div.orangehrm-login-slot-wrapper div.orangehrm-login-slot div.orangehrm-login-form form.oxd-form div.oxd-form-actions.orangehrm-login-action:nth-child(4) > button.oxd-button.oxd-button--medium.oxd-button--main.orangehrm-login-button')))
#while len(results) == 0 :
#    results = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'div.orangehrm-login-layout div.orangehrm-login-layout-blob div.orangehrm-login-container div.orangehrm-login-slot-wrapper div.orangehrm-login-slot div.orangehrm-login-form form.oxd-form div.oxd-form-actions.orangehrm-login-action:nth-child(4) > button.oxd-button.oxd-button--medium.oxd-button--main.orangehrm-login-button')))
#    print(results)
#    print(len(results))

username=WebDriverWait(chromedriver,30).until(EC.element_to_be_clickable((By.NAME,"username")))
username.clear()
username.send_keys("Admin")

password=WebDriverWait(chromedriver,30).until(EC.element_to_be_clickable((By.NAME,"password")))

password.clear()
password.send_keys('admin123')

login=WebDriverWait(chromedriver,30).until(EC.element_to_be_clickable((By.TAG_NAME,"button")))
login.click()

#6. What is the difference in TestNG between BeforeMethod, BeforeClass, and BeforeTest?
#@BeforeMethod: Runs before each test method. Useful for setting up test-specific data.
#@BeforeClass: Runs once before the first test method in the class. Useful for class-level setup.
#@BeforeTest: Runs before any test method in the <test> tag in the XML configuration file. Useful for setting up configurations or data before any tests in a test suite.

#Search from Dropdown List
#select_element = WebDriverWait(chromedriver, 10).until(
#        EC.presence_of_element_located((By.XPATH,"//select[@id='customerCurrency']"))
#)
# Create a Select object
#select = Select(select_element)

# Select an option by index
###select.select_by_index(1)
#time.sleep(3)
#select.select_by_visible_text('US Dollar')
#time.sleep(5)