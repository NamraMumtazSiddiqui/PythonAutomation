import time
from selenium import webdriver

# Initialize WebDriver
driver = webdriver.Chrome()

# Open a website
driver.get('https://example.com')

# Open a new window or tab (simulate opening a new window)
driver.execute_script("window.open('https://www.google.com', '_blank');")
time.sleep(10)
driver.execute_script("window.open('https://www.bing.com', '_blank');")
time.sleep(10)

# Get all window handles by this Property
window_handles = driver.window_handles
print(f"Number of windows open: {len(window_handles)}")

# Move to a Child Window Based on a Specific Page Title Condition
def switch_to_child_window(driver,title):
    for handle in window_handles:
        driver.switch_to.window(handle)
        if(driver.title==title):
            print(f"Switch to window with title:{title}")
            return True
    return False

switch_to_child_window(driver,"Google")

#3. Verify Expected Page Titles Among Child Windows and Navigate Accordingly
Expected_titles=['Bing','Google']

for title in Expected_titles:
    if switch_to_child_window(driver,title):
        print(f"Verified Titles: {title}")

driver.quit()