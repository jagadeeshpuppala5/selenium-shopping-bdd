import json
from selenium import webdriver


def get_driver():
    with open("config/config.json") as f:
        config = json.load(f)

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(config["base_url"])
    return driver
