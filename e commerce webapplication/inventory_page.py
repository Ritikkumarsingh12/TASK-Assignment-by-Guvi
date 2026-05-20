import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage

class InventoryPage(BasePage):
    """Page Object for the Product Catalog Page."""
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    INVENTORY_ITEM = (By.CLASS_NAME, "inventory_item")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "button[id^='add-to-cart']")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    RESET_LINK = (By.ID, "reset_sidebar_link")

    def is_cart_visible(self):
        return self.is_displayed(self.CART_ICON)

    def select_random_products(self, count=4):
        """Randomly selects N products and returns their details ."""
        items = self.driver.find_elements(*self.INVENTORY_ITEM)
        selected_items = random.sample(items, count)
        
        product_data = []
        for item in selected_items:
            name = item.find_element(*self.ITEM_NAME).text
            price = item.find_element(*self.ITEM_PRICE).text
            # Use dynamic matching to click the button within this specific item container
            btn = item.find_element(*self.ADD_TO_CART_BTN)
            product_data.append({"name": name, "price": price, "button": btn})
        return product_data

    def get_cart_badge_count(self):
        if self.is_displayed(self.CART_BADGE):
            return int(self.get_text(self.CART_BADGE))
        return 0

    def navigate_to_cart(self):
        self.click(self.CART_ICON)

    def change_sorting(self, option_text):
        dropdown = Select(self.driver.find_element(*self.SORT_DROPDOWN))
        dropdown.select_by_visible_text(option_text)

    def get_all_product_names(self):
        elements = self.driver.find_elements(*self.ITEM_NAME)
        return [el.text for el in elements]

    def get_all_product_prices(self):
        elements = self.driver.find_elements(*self.ITEM_PRICE)
        return [float(el.text.replace("$", "")) for el in elements]

    def trigger_sidebar_action(self, action_type):
        self.click(self.MENU_BUTTON)
        # Ensure smooth visual transition wait
        import time; time.sleep(0.5)
        if action_type == "logout":
            self.click(self.LOGOUT_LINK)
        elif action_type == "reset":
            self.click(self.RESET_LINK)