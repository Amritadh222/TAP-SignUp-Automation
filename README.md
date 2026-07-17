# QA Automation Project

This repository contains a Selenium + Pytest automation flow for a signup journey that verifies a one-time password (OTP) sent by email.

## What the project does

The test in [tests/test_Signup.py](tests/test_Signup.py) performs the following steps:

1. Opens the target application URL from `BASE_URL`
2. Fills in the signup form with values from the environment
3. Waits for the verification email to arrive
4. Extracts the OTP from the inbox using IMAP polling
5. Enters the OTP on the verification page and submits the form

## Project structure

- [conftest.py](conftest.py): pytest fixtures for the Selenium driver, base URL, credentials, and OTP helper
- [requirements.txt](requirements.txt): Python dependencies
- [Pages/base_page.py](Pages/base_page.py): shared Selenium page-object helpers
- [Pages/signUp_page.py](Pages/signUp_page.py): signup page object
- [Pages/verify_page.py](Pages/verify_page.py): verification page object for OTP entry
- [tests/test_Signup.py](tests/test_Signup.py): end-to-end signup test
- [utils/email_helper.py](utils/email_helper.py): Gmail IMAP polling utility for retrieving OTP codes

## Prerequisites

- Python 3.10+
- Google Chrome installed
- ChromeDriver available on the system path, or Selenium Manager can resolve it automatically
- A mailbox that can be accessed through IMAP for OTP retrieval

## Environment setup

Create a `.env` file in the project root and define the variables below:

```env
BASE_URL=https://your-app-url
FIRST_NAME_INPUT=John
LAST_NAME_INPUT=Doe
EMAIL_INPUT=john.doe@example.com
PHONE_NUMBER_INPUT=1234567890
PASSWORD_INPUT=StrongPassword123
CONFIRM_PASSWORD_INPUT=StrongPassword123

EMAIL_IMAP_HOST=imap.gmail.com
EMAIL_ADDRESS=your-email@example.com
EMAIL_APP_PASSWORD=your-gmail-app-password
```

### Notes

- `EMAIL_ADDRESS` should be the account receiving the verification email.
- `EMAIL_APP_PASSWORD` must be a Gmail App Password, not your normal account password.
- `BASE_URL` should point to the signup page or application entry URL used by the test.

## Install dependencies

```bash
pip install -r requirements.txt
```

## Run the test

```bash
pytest tests/test_Signup.py -v
```

## Email OTP helper

You can also test the email polling logic separately before running the full flow:

```bash
python utils/email_helper.py
```

This is useful for verifying that the IMAP connection, login credentials, and OTP extraction logic are working correctly.

## Current automation behavior

The current implementation is configured to:

- use Gmail IMAP polling through [utils/email_helper.py](utils/email_helper.py)
- search for new emails from `theauthorizedpartner.com`
- extract a 6-digit OTP from the email body
- submit the OTP through the verification page object in [Pages/verify_page.py](Pages/verify_page.py)

If the real application's email sender or OTP format changes, update the filtering logic in [utils/email_helper.py](utils/email_helper.py) and the verification page locators in [Pages/verify_page.py](Pages/verify_page.py) accordingly.
