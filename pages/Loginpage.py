from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
import time


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.email_input = (By.XPATH, "//input[@data-qa='login-email']")
        self.password_input = (By.XPATH, "//input[@data-qa='login-password']")
        self.login_button = (By.XPATH, "//button[@data-qa='login-button']")  # use stable data-qa locator
        self.logged_in_text = (By.XPATH, "//a[contains(text(), 'Logged in as')]")
        self.error_message = (By.XPATH, "//p[contains(text(), 'Your email or password is incorrect!')]")

    def login(self, email, password):
        wait = WebDriverWait(self.driver, 10)

        # Wait for input fields
        wait.until(EC.visibility_of_element_located(self.email_input)).send_keys(email)
        wait.until(EC.visibility_of_element_located(self.password_input)).send_keys(password)

        # Wait until login button is clickable
        login_btn = wait.until(EC.element_to_be_clickable(self.login_button))

        # Scroll into view to avoid overlap
        self.driver.execute_script("arguments[0].scrollIntoView(true);", login_btn)
        time.sleep(1)  # short pause for smooth rendering

        try:
            login_btn.click()
        except ElementClickInterceptedException:
            # Remove ad iframes dynamically
            self.driver.execute_script("""
                var ads = document.querySelectorAll('iframe[id^="aswift_"], iframe[id^="google_ads"]');
                ads.forEach(a => a.remove());
            """)
            time.sleep(1)
            # Fallback: JS click
            self.driver.execute_script("arguments[0].click();", login_btn)

    def get_login_message(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.logged_in_text)
        ).text

    def get_error_message(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.error_message)
        ).text
