from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DashboardPage(BasePage):

    profile_icon = (By.XPATH, "//img[contains(@class,'profile')]")
    logout_button = (By.XPATH, "//button[contains(text(),'Logout')]")

    def is_dashboard_loaded(self):
        return self.is_displayed(self.profile_icon)

    def logout(self):
        self.click_element(self.profile_icon)
        self.click_element(self.logout_button)