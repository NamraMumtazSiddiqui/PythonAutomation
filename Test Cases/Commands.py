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

# Different types of Commands
#1-Application Commands
# title , current_url , page_source

print(driver1.title)
print(driver1.current_url)
print(driver1.page_source)

#2-Conditional Commands
# is_displayed () , is_enabled () , is_selected ()
searchbox=driver1.find_element(By.XPATH,"//input[@id='small-searchterms']")
print("display status :", searchbox.is_displayed())
print("display status : ", searchbox.is_displayed())

#Is selected for Radio Buttons
radionutton1=driver1.find_element(By.XPATH,"//input[@id='pollanswers-1']")
print("display status : ", radionutton1.is_selected())

radionutton1.click()
time.sleep(5)
radionutton2=driver1.find_element(By.XPATH,"//input[@id='pollanswers-2']")
print("display status : ", radionutton2.is_selected())


#After selecting radio button
print("After selecting Excellent radio button")
print(radionutton1.is_selected())
print(radionutton2.is_selected())
#3-Browser Commands
#quit() and #close()
