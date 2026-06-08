import random

class ProductsPage:

    def __init__(self, page):
        self.page = page

    def cart_visible(self):
        return self.page.locator(".shopping_cart_link").is_visible()

    def get_products(self):
        return self.page.locator(".inventory_item")

    def select_random_products(self, count=4):

        products = self.get_products()

        total = products.count()

        selected = random.sample(range(total), count)

        names = []

        for index in selected:

            product = products.nth(index)

            name = product.locator(".inventory_item_name").text_content()

            product.locator("button").click()

            names.append(name)

        return names

    def cart_count(self):
        return self.page.locator(".shopping_cart_badge").text_content()

    def open_cart(self):
        self.page.click(".shopping_cart_link")

    def logout(self):

        self.page.click("#react-burger-menu-btn")

        self.page.click("#logout_sidebar_link")

    def reset_app_state(self):

        self.page.click("#react-burger-menu-btn")

        self.page.click("#reset_sidebar_link")

    def sort_products(self, value):
        self.page.select_option(".product_sort_container", value)