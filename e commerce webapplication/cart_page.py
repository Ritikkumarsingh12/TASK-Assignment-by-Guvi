from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    """Page Object for the Cart Summary Page."""
    CART_ITEM = (By.CLASS_NAME, "cart_item")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def get_cart_items_details(self):
        items = self.driver.find_elements(*self.CART_ITEM)
        details = {}
        for item in items:
            name = item.find_element(*self.ITEM_NAME).text
            price = item.find_element(*self.ITEM_PRICE).text
            details[name] = price
        return details

    def proceed_to_checkout(self):
        self.click(self.CHECKOUT_BUTTON)