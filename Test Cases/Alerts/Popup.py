from datetime import time
from selenium import webdriver
from selenium.common import UnexpectedTagNameException
from selenium.webdriver.chrome.service import Service

class DemoPopUp():
    def demo_js_alerts(self):
        driver_path = r"C:\Users\HP\Downloads\Chromedrivers\Drivers\chromedriver.exe"
        # Set up the ChromeDriver Service
        serviceobj = Service(driver_path)
        # Initialize the Chrome WebDriver with the service
        driver1 = webdriver.Chrome(service=serviceobj)
        # Create a new Chrome browser instance
        driver1.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_confirm")
