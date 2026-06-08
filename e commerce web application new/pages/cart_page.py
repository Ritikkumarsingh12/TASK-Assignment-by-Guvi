class CartPage:

    def __init__(self, page):
        self.page = page

    def get_cart_items(self):

        items = self.page.locator(".inventory_item_name")

        return [items.nth(i).text_content()
                for i in range(items.count())]

    def checkout(self):
        self.page.click("#checkout")