from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    email_input = (By.ID, 'email')
    password_input = (By.ID, 'password')
    login_button = (By.ID, 'login-btn')
    error_message = (By.CLASS_NAME, 'invalid-feedback')

    def enter_email(self, email):
        self.enter_text(self.email_input, email)

    def enter_password(self, password):
        self.enter_text(self.password_input, password)

    def click_login_button(self):
        self.click_element(self.login_button)

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()

    def is_error_displayed(self):
        return self.is_displayed(self.error_message)

.signup_btn)