from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    """Page Object for Information submission, Overview, and Completion fields."""
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    CONFIRM_HEADER = (By.CLASS_NAME, "complete-header")

    def fill_user_details(self, fname, lname, zip_code):
        self.send_keys(self.FIRST_NAME, fname)
        self.send_keys(self.LAST_NAME, lname)
        self.send_keys(self.POSTAL_CODE, zip_code)
        self.click(self.CONTINUE_BUTTON)

    def complete_order(self):
        self.click(self.FINISH_BUTTON)

    def get_confirmation_msg(self):
        return self.get_text(self.CONFIRM_HEADER)