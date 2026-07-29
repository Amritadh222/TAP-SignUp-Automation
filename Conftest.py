import os
from dotenv import load_dotenv
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

load_dotenv()  # Load environment variables from .env file


@pytest.fixture
def driver():
    # Initialize the WebDriver (e.g., Chrome)
    driver = webdriver.Chrome()  # or any other browser driver
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def base_url():
    return os.getenv("BASE_URL")


@pytest.fixture
def credentials():
    return {
        "firstname": os.getenv("FIRST_NAME_INPUT"),
        "lastname": os.getenv("LAST_NAME_INPUT"),
        "email": os.getenv("EMAIL_INPUT"),
        "phone_number": os.getenv("PHONE_NUMBER_INPUT"),
        "password": os.getenv("PASSWORD_INPUT"),
        "confirm_password": os.getenv("CONFIRM_PASSWORD_INPUT"),
    }


@pytest.fixture
def otp():
    """
    Returns the get_otp_from_email function so tests can call:
        code = otp(subject_filter="Verify")
    """
    from utils.email_helper import get_otp_from_email
    return get_otp_from_email

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # We only look at actual failing test calls, not setup/teardown
    if rep.when == "call" and rep.failed:
        driver = item.funcargs['driver']
        test_name = item.name
        from screenshot_utility import take_screenshot
        take_screenshot(driver, test_name)