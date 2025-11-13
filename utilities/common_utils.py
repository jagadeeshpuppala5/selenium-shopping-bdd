import os
from datetime import datetime

def take_screenshot(driver, name):
    folder = "screenshots"
    os.makedirs(folder, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    driver.save_screenshot(f"{folder}/{name}_{timestamp}.png")
