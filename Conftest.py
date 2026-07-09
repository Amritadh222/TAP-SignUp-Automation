import pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    # Initialize the WebDriver (e.g., Chrome)
    driver = webdriver.Chrome()  # You can specify the path to the ChromeDriver if needed
    driver.maximize_window()
    yield driver
    driver.quit()