import os
from datetime import datetime

def take_screenshot(driver, test_name):
    # Create a directory for screenshots if it doesn't exist
    screenshot_dir = "screenshots"
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)

    # Generate a timestamp for the screenshot filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_filename = f"{test_name}_{timestamp}.png"
    screenshot_path = os.path.join(screenshot_dir, screenshot_filename)

    # Take the screenshot and save it to the specified path
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved to: {screenshot_path}")