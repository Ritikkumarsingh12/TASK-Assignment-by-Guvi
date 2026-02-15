from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    profile_icon = (By.XPATH, "//img[@alt='profile']")
    logout_button = (By.XPATH, "//button[contains(text(),'Logout')]")

    def logout(self):
        self.wait.until(EC.element_to_be_clickable(self.profile_icon)).click()
        self.wait.until(EC.element_to_be_clickable(self.logout_button)).click()
