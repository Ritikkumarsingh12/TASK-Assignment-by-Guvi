from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):

    login_btn = (By.LINK_TEXT, 'Login')
    signup_btn = (By.LINK_TEXT, 'Sign up')

    def click_login(self):
        self.click_element(self.login_btn)

    def click_signup(self):
        self.click_element(self.signup_btn)

    def is_login_visible(self):
        return self.is_displayed(self.login_btn)

    def is_signup_visible(self):
        return self.is_displayed(self.signup_btn)