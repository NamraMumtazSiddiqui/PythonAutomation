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

#4-Navigational Commands
# back () , forward () and refresh ()
driver1.get("https://www.google.com")
driver1.get("https://www.amazon.com")
driver1.back()
time.sleep(5)
driver1.forward()
driver1.refresh()
time.sleep(5)

driver1.close()
#5-Wait Commands

