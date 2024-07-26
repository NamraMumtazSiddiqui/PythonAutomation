from selenium import webdriver


# Path to the chromedriver executable
driver= webdriver.Chrome("")

# Initialize the WebDriver with the service object
# Open a webpage to test
driver.get("https://dev2.innotech-sa.com/AssessmentSystemV2/Master/System/")
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//input[@id='txtUsername']").send_keys("ca_kingfaisal")
driver.implicitly_wait(20)
driver.find_element(By.XPATH,"//input[@id='txtPassword']").send_keys("Asdfg098@")
driver.implicitly_wait(20)
driver.find_element(By.XPATH,"//button[@id='btnAuthenticate']").click()
