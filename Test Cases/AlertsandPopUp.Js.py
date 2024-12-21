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

class PopUp() :
 def alerts(self):
     driver_path = r"C:\Users\HP\Downloads\Chromedrivers\Drivers\chromedriver.exe"
     serviceobj = Service(driver_path)
     driver1 = webdriver.Chrome(service=serviceobj)

     driver1.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_confirm")
     driver1.switch_to.frame("iframeResult")

     # For OK , its Accept Alert and show pop up text
     driver1.find_element(By.XPATH, "//button[normalize-space()='Try it']").click()
     time.sleep(2)
     print(driver1.switch_to.alert.accept())
     print(driver1.switch_to.alert.text)
     time.sleep(2)

     # For Cancel , its Dismiss Alert
     driver1.find_element(By.XPATH, "//button[normalize-space()='Try it']").click()
     time.sleep(2)
     driver1.switch_to.alert.dismiss()
     time.sleep(2)

     # For sending text in alert
     driver1.find_element(By.XPATH, "//button[normalize-space()='Try it']").click()
     time.sleep(2)
     driver1.switch_to.alert.send_keys("Test Keys")
     driver1.switch_to.alert.accept()
     time.sleep(2)


obj=PopUp()
obj.alerts()


