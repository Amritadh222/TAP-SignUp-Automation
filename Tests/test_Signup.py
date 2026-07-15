from Pages.signUp_page import SignUpPage
import time

def test_Signup(driver,base_url,credentials):
    sign_up=SignUpPage(driver)
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