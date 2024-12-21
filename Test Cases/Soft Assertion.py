import pytest
from selenium import webdriver


def test_multiple_conditions():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/auth/login")

    errors = []

    try:
        assert driver.title == "Demo"
    except AssertionError as e:
        errors.append(str(e))

    try:
        assert driver.current_url=="https://opensource-demo.orangehrmlive.com/auth/login"
    except AssertionError as e:
        errors.append(str(e))

    # After checking all conditions, raise AssertionError if any failed
    if errors:
        pytest.fail(f"Errors occurred: {errors}")

    driver.quit()
