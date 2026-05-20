import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """Base class providing core Selenium wrapper functions with dynamic waits."""
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Dynamic wait handling 

    def click(self, locator):
        try:
            self.wait.until(EC.element_to_be_clickable(locator)).click()
        except Exception as e:
            print(f"Error clicking element {locator}: {e}")
            raise

    def send_keys(self, locator, text):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            element.clear()
            element.send_keys(text)
        except Exception as e:
            print(f"Error entering text into element {locator}: {e}")
            raise

    def get_text(self, locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(locator)).text
        except Exception as e:
            print(f"Error fetching text from element {locator}: {e}")
            raise

    def is_displayed(self, locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()
        except Exception:
            return False

    def take_screenshot(self, filename):
        os.makedirs("screenshots", exist_ok=True)
        self.driver.save_screenshot(f"screenshots/{filename}")