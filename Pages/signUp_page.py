from selenium.webdriver.common.by import By
from .base_page import BasePage

class SignUpPage(BasePage):
    # Locators
    FIRST_NAME_INPUT = (By.ID, "firstName")
    LAST_NAME_INPUT = (By.ID, "lastName")
    EMAIL_INPUT = (By.ID, "email")  
    PHONE_NUMBER_INPUT = (By.ID, "phoneNumber")
    PASSWORD_INPUT = (By.ID, "password")
    CONFIRM_PASSWORD_INPUT = (By.ID, "confirmPassword")
    sign_up_button = (By.ID, "signUpButton")

    def load(self):
        self.open("https://authorized-partner.vercel.app/register?step=setup")

    def sign_up(self, firstname: str, lastname: str, email: str, phoneNumber: int, password: str, confirmPassword: str):
        self.type(self.FIRST_NAME_INPUT, firstname)
        self.type(self.LAST_NAME_INPUT, lastname)
        self.type(self.EMAIL_INPUT, email)
        self.type(self.PHONE_NUMBER_INPUT, phoneNumber)
        self.type(self.PASSWORD_INPUT, password)
        self.type(self.CONFIRM_PASSWORD_INPUT, confirmPassword)
        self.click(self.sign_up_button)