import os
from datetime import datetime


def take_screenshot(driver, test_name):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    screenshots_dir = os.path.join(base_dir, "reports", "screenshots")

    os.makedirs(screenshots_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_name = f"{test_name}_{timestamp}.png"
    file_path = os.path.join(screenshots_dir, file_name)

    driver.save_screenshot(file_path)
    return file_path
