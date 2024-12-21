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
# Service Object: The service parameter tells the webdriver.Chrome constructor
# to use the serviceobj object created earlier. This object encapsulates the path to the ChromeDriver
# executable and manages its lifecycle.

#Class and Constructor
#A constructor is a special type of method that is automatically called when an object of
# the class is created. Its primary role is to initialize the object's attributes.

# designed to initialize objects of a class.
#The Chrome() constructor can take multiple optional parameters, such as service and options

driver1 = webdriver.Chrome(service=serviceobj)

# Create a new Chrome browser instance
driver1.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# Find username and password input fields and submit button
username1= WebDriverWait(driver1,30).until(
    EC.element_to_be_clickable((By.NAME,"username"))
)
username1.clear()
username1.send_keys("Admin")

password1 = WebDriverWait(driver1, 30).until(
    EC.element_to_be_clickable((By.NAME, "password"))
)
password1.clear()
password1.send_keys("admin123")

login = WebDriverWait(driver1, 10).until(
   EC.element_to_be_clickable((By.TAG_NAME, "button"))
)
# Enter username and password
# Click the login button
login.click()
# Wait for the login process to complete

Adminpage = WebDriverWait(driver1, 10).until(
    EC.element_to_be_clickable((By.XPATH,"//body/div[@id='app']/div[1]/div[1]/aside[1]/nav[1]/div[2]/ul[1]/li[1]/a[1]"))
)
Adminpage.click()


username= WebDriverWait(driver1,timeout=30).until(EC.element_to_be_clickable(By.TAG_NAME,"username"))
username.clear()
username.send_keys("Test Account")

password=WebDriverWait(driver1,timeout=30).until(EC.element_to_be_clickable((By.TAG_NAME,"password")))



Username=WebDriverWait(driver1,20).until(EC.element_to_be_clickable(By.TAG_NAME,"button"))
