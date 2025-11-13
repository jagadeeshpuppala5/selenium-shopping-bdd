from selenium.webdriver.common.by import By


class SignupPage:
    def __init__(self,driver):
        self.driver = driver
        self.name_input = (By.NAME, "name")
        self.email_input = (By.XPATH, "//input[@data-qa='signup-email']")
        self.signup_button = (By.XPATH, "//button[text()='Signup']")

    def signup(self, name, email):
        self.driver.find_element(*self.name_input).send_keys(name)
        self.driver.find_element(*self.email_input).send_keys(email)
        self.driver.find_element(*self.signup_button).click()
