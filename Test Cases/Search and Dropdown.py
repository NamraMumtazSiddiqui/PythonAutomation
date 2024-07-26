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
# Path to your chromedriver executable
driver_path = r"C:\Users\HP\Downloads\Chromedrivers\Drivers\chromedriver.exe"

# Set up the ChromeDriver Service
# Service Class: An instance of the Service class is created. This class is responsible for starting
# and stopping the ChromeDriver executable.
# driver_path: This is the path to the ChromeDriver executable on your local machine.
serviceobj = Service(driver_path)

# Initialize the Chrome WebDriver with the service
# Service Object: The serviceobj=service parameter tells the webdriver.Chrome constructor
# to use the serviceobj object created earlier. This object encapsulates the path to the ChromeDriver
# executable and manages its lifecycle.
#Class and Constructor
#a constructor itself is not an object. It is a special method
# designed to initialize objects of a class.

driver1 = webdriver.Chrome(service=serviceobj)

driver1.get("https://demo.nopcommerce.com/")

#Search Field

search = WebDriverWait(driver1, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@id='small-searchterms']"))
)
search.send_keys('Adobe')
time.sleep(5)

send_search = WebDriverWait(driver1, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Search')]"))
)
send_search.click()
time.sleep(5)


#Search from Dropdown List
select_element = WebDriverWait(driver1, 10).until(
        EC.presence_of_element_located((By.XPATH,"//select[@id='customerCurrency']"))
)
# Create a Select object
select = Select(select_element)

# Select an option by index
select.select_by_visible_text('US Dollar')
time.sleep(4)
select.select_by_index(1)
time.sleep(3)
select.select_by_visible_text('US Dollar')
time.sleep(4)

