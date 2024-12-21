import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class TestOrangeHRM:

    @pytest.fixture()
    def setup(self):
        driver_path = r"C:\Users\HP\Downloads\Chromedrivers\Drivers\chromedriver.exe"
        service_obj = Service(driver_path)
        self.driver = webdriver.Chrome(service=service_obj)
        self.driver.maximize_window()

        yield self.driver
        self.driver.quit()

    @pytest.mark.smoke
    def test_homepagetitle(self, setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/auth/login")
        assert self.driver.title == 'OrangeHRM', "Title does not match"

    def test_login(self, setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/auth/login")

        # Wait for the username field and enter the username
        username_field = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.NAME, "username"))
        )
        username_field.clear()
        username_field.send_keys("Admin")

        # Wait for the password field and enter the password
        password_field = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.NAME, "password"))
        )
        password_field.clear()
        password_field.send_keys("admin123")

        # Click the login button
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.TAG_NAME, "button"))
        )
        login_button.click()

        # Assert that login was successful by checking for the presence of an element after login
        dashboard_element = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, "dashboard"))
        )
        assert dashboard_element is not None, "Login failed!"
