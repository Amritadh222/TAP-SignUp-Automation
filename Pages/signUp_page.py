from selenium.webdriver.common.by import By
from .base_page import BasePage

class SignUpPage(BasePage):
    # Locators
    FIRST_NAME_INPUT = (By.XPATH, "//input[@id='_R_j5bav4npfnb_-form-item']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@id='_R_135bav4npfnb_-form-item']")
    EMAIL_INPUT = (By.XPATH, "//input[@id='_R_l5bav4npfnb_-form-item']")  
    PHONE_NUMBER_INPUT = (By.XPATH, "//input[@id='_R_355bav4npfnb_-form-item']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    CONFIRM_PASSWORD_INPUT = (By.XPATH, "//input[@name='confirmPassword']")
    sign_up_button = (By.XPATH, "//button[normalize-space()='Next']")

    def load(self,base_url: str):
        self.open(base_url)

    def sign_up(self, firstname: str, lastname: str, email: str, phoneNumber: str, password: str, confirmPassword: str):
        self.type(self.FIRST_NAME_INPUT, firstname)
        self.type(self.LAST_NAME_INPUT, lastname)
        self.type(self.EMAIL_INPUT, email)
        self.type(self.PHONE_NUMBER_INPUT, phoneNumber)
        self.type(self.PASSWORD_INPUT, password)
        self.type(self.CONFIRM_PASSWORD_INPUT, confirmPassword)
        self.click(self.sign_up_button)