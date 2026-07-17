import time
from datetime import datetime, timezone
from Pages.signUp_page import SignUpPage
from Pages.verify_page import VerifyPage


def test_Signup(driver, base_url, credentials, otp):
    start_time = datetime.now(timezone.utc)

    sign_up = SignUpPage(driver)
    sign_up.load(base_url)
    time.sleep(2)
    sign_up.sign_up(
        firstname=credentials["firstname"],
        lastname=credentials["lastname"],
        email=credentials["email"],
        phoneNumber=credentials["phone_number"],
        password=credentials["password"],
        confirmPassword=credentials["confirm_password"]
    )

    code = otp(sender_filter="theauthorizedpartner.com", since_start=start_time)

    verify = VerifyPage(driver)
    verify.enter_otp(code)