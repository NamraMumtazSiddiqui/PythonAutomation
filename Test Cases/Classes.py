from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Path to your chromedriver executable
driver_path = r"C:\Users\HP\Downloads\Chromedrivers\Drivers\chromedriver.exe"

# Set up the ChromeDriver Service
serviceobj = Service(driver_path)

# Initialize the Chrome WebDriver with the service
driver = webdriver.Chrome(service=serviceobj)

#__init__ is a special method in Python, known as the constructor.
# It is automatically called when an object of the class is created.

# By assigning self.driver = driver, you make driver accessible to all other methods within the OrangeHRM class.
# This allows you to use instance attribute self.driver in any other method within the class to interact with the WebDriver.

class OrangeHRM:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        #Without self.driver, you’d need to pass the driver explicitly to each method or create a new
        # instance of WebDriver every time, which would complicate the code and result in multiple
        # browser windows opening.

        # Open the login page
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(2)
        # Enter username and password and click the login button
        self.driver.find_element(By.NAME, "username").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        print("Logged in successfully.")
        time.sleep(3)
        self.driver.save_screenshot(r"C:\Users\HP\PycharmProjects\Test Automation-786\Screenshots\FirstScreenshot.png")
    def logout(self):
        # Code for logging out of the application
        print("Attempting to log out...")
        try:
            # Example selector (modify if actual selector differs)
            self.driver.find_element(By.ID, "logoutButton").click()
            print("Logged out successfully.")
        except NoSuchElementException:
            print("Logout button not found.")

    def navigate_to_dashboard(self):
        # Code for navigating to the dashboard
        print("Navigating to the dashboard...")
        try:
            # Example navigation code (modify if actual selector differs)
            self.driver.find_element(By.ID, "dashboardLink").click()
            print("Dashboard opened.")
        except NoSuchElementException:
            print("Dashboard link not found.")

# Create an instance of the OrangeHRM class and call methods
#The driver parameter is stored in the instance variable self.driver. This encapsulation allows all methods
# within the OrangeHRM class to use the same WebDriver instance, maintaining the browser session.

orange_hrm = OrangeHRM(driver)
orange_hrm.login("Admin", "admin123")

# Wait to observe the result or take other actions if needed
time.sleep(3)

# Close the driver after execution
driver.quit()
