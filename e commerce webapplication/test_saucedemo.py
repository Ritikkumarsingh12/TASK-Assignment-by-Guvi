import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@pytest.mark.usefixtures("setup")
class TestSauceDemo:
    
    # Class-level state sharing for workflow continuation
    stored_products = []

    # --- Test-Case-1: Login with various predefined users ---
    @pytest.mark.parametrize("username, status", [
        ("standard_user", "valid"),
        ("locked_out_user", "invalid"),
        ("problem_user", "valid"),
        ("performance_glitch_user", "valid")
    ])
    def test_case_1_login_profiles(self, username, status):
        login_page = LoginPage(self.driver)
        inventory_page = InventoryPage(self.driver)
        
        login_page.login(username, "secret_sauce")
        
        if status == "valid":
            assert inventory_page.is_cart_visible() is True 
            # Reset view to home screen for the next parameter iteration
            inventory_page.trigger_sidebar_action("logout")
        else:
            assert "Epic sadface:" in login_page.get_error_message()
            self.driver.refresh()

    # --- Test-Case-2: Login with invalid credentials ---
    def test_case_2_invalid_login(self):
        login_page = LoginPage(self.driver)
        login_page.login("invalid_user", "wrong_password")
        assert "Epic sadface:" in login_page.get_error_message()
        self.driver.refresh()

    # --- Test-Case-3 & 4: Validate logout & standard initialization ---
    def test_case_3_4_lifecycle(self):
        login_page = LoginPage(self.driver)
        inventory_page = InventoryPage(self.driver)
        
        login_page.login("standard_user", "secret_sauce")
        assert inventory_page.is_cart_visible() is True  # Test-Case-4 
        
        inventory_page.trigger_sidebar_action("logout")
        assert "login-button" in self.driver.current_url or login_page.is_displayed(LoginPage.LOGIN_BUTTON)  # Test-Case-3 

    # --- Test-Case-5: Random selection and extraction ---
    def test_case_5_extract_random_products(self):
        login_page = LoginPage(self.driver)
        inventory_page = InventoryPage(self.driver)
        
        login_page.login("standard_user", "secret_sauce")
        TestSauceDemo.stored_products = inventory_page.select_random_products(4) 
        
        print("\n--- Extracted Products ---")
        for item in TestSauceDemo.stored_products:
            print(f"Product: {item['name']} | Price: {item['price']}") 
        
        assert len(TestSauceDemo.stored_products) == 4

    # --- Test-Case-6: Add selected products to cart ---
    def test_case_6_add_to_cart_validate(self):
        inventory_page = InventoryPage(self.driver)
        
        for item in TestSauceDemo.stored_products:
            item['button'].click()
            
        assert inventory_page.get_cart_badge_count() == 4 

    # --- Test-Case-7: Validate product details inside cart ---
    def test_case_7_verify_cart_items(self):
        inventory_page = InventoryPage(self.driver)
        cart_page = CartPage(self.driver)
        
        inventory_page.navigate_to_cart() 
        ui_cart_details = cart_page.get_cart_items_details()
        
        for expected_item in TestSauceDemo.stored_products:
            name = expected_item['name']
            price = expected_item['price']
            assert name in ui_cart_details 
            assert ui_cart_details[name] == price 

    # --- Test-Case-8: Complete checkout and validate order ---
    def test_case_8_checkout_flow(self):
        cart_page = CartPage(self.driver)
        checkout_page = CheckoutPage(self.driver)
        
        cart_page.proceed_to_checkout() 
        checkout_page.fill_user_details("John", "Doe", "12345") 
        
        # Capture Order Summary Screenshot 
        checkout_page.take_screenshot("order_summary.png")
        
        checkout_page.complete_order() 
        assert "Thank you for your order!" in checkout_page.get_confirmation_msg() 
        
        # Navigate back to item inventory catalog
        self.driver.get("https://www.saucedemo.com/inventory.html")

    # --- Test-Case-9: Validate sorting functionality ---
    def test_case_9_sorting(self):
        inventory_page = InventoryPage(self.driver)
        
        # Test Z to A 
        inventory_page.change_sorting("Name (Z to A)") 
        names = inventory_page.get_all_product_names()
        assert names == sorted(names, reverse=True) 
        
        # Test Price Low to High 
        inventory_page.change_sorting("Price (low to high)") 
        prices = inventory_page.get_all_product_prices()
        assert prices == sorted(prices) 

    # --- Test-Case-10: Validate Reset App State ---
    def test_case_10_reset_state(self):
        inventory_page = InventoryPage(self.driver)
        
        # Add an item to observe status switch state changes
        products = inventory_page.select_random_products(1)
        products[0]['button'].click()
        assert inventory_page.get_cart_badge_count() > 0
        
        # Fire application execution reset criteria 
        inventory_page.trigger_sidebar_action("reset") 
        
        assert inventory_page.get_cart_badge_count() == 0