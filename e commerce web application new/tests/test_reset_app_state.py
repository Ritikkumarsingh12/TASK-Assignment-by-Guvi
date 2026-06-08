from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from utils.config import *

def test_reset_app_state(page):

    LoginPage(page).login(
        STANDARD_USER,
        PASSWORD
    )

    products = ProductsPage(page)

    products.select_random_products(4)

    products.reset_app_state()

    page.reload()

    badge = page.locator(".shopping_cart_badge")

    assert badge.count() == 0