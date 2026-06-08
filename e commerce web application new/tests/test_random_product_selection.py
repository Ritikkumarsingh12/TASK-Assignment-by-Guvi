from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from utils.config import *

def test_cart_validation(page):

    LoginPage(page).login(
        STANDARD_USER,
        PASSWORD
    )

    products = ProductsPage(page)

    selected = products.select_random_products(4)

    products.open_cart()

    cart_items = CartPage(page).get_cart_items()

    assert sorted(selected) == sorted(cart_items)"