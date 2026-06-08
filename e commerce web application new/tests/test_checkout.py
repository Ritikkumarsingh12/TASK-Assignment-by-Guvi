from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.config import *

def test_checkout(page):

    LoginPage(page).login(
        STANDARD_USER,
        PASSWORD
    )

    products = ProductsPage(page)

    products.select_random_products(4)

    products.open_cart()

    CartPage(page).checkout()

    checkout = CheckoutPage(page)

    checkout.enter_user_info(
        "Ritik",
        "Tomer",
        "201001"
    )

    checkout.finish_order()

    assert "Thank You" in \
           checkout.confirmation_message()