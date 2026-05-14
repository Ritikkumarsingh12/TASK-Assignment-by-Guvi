from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException

class LoginPage(BasePage):

    username_input = (By.NAME, "username")
    password_input = (By.NAME, "password")
    login_button = (By.XPATH, "//button[@type='submit']")
    dashboard_text = (By.XPATH, "//h6[text()='Dashboard']")
    error_message = (By.XPATH, "//p[contains(text(),'Invalid')]")
    profile_dropdown = (By.CLASS_NAME, "oxd-userdropdown-tab")
    logout_button = (By.XPATH, "//a[text()='Logout']")

    def login(self, username, password):
        self.enter_text(self.username_input, username)
        self.enter_text(self.password_input, password)
        self.click_element(self.login_button)

    def is_dashboard_displayed(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.dashboard_text))
            return True
        except TimeoutException:
            return False

    def is_error_displayed(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.error_message))
            return True
        except TimeoutException:
            return False

    def logout(self):
        self.click_element(self.profile_dropdown)
        self.click_element(self.logout_button)