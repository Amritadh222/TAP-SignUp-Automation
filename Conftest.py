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
