import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class VerifyPage(BasePage):
    OTP_INPUT = (By.XPATH, "//input[@data-input-otp='true']")
    VERIFY_BUTTON = (By.XPATH, "//button[normalize-space()='Verify Code']")

    def enter_otp(self, code: str):
        elem = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.OTP_INPUT)
        )
        elem.click()
        time.sleep(0.3)
        for digit in code:
            elem.send_keys(digit)
            time.sleep(0.15)

        # Give React a moment to process the last keystroke and enable the button
        time.sleep(1)

        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.VERIFY_BUTTON)
        )

        try:
            button.click()
        except Exception:
            # Fallback: force a JS click if the normal click gets
            # intercepted (e.g. by an overlapping pointer-events:none layer)
            self.driver.execute_script("arguments[0].click();", button)

        time.sleep(1)  # let the page react/navigate before the test ends