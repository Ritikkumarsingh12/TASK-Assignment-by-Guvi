from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from utils.config import *

def test_cart_visibility(page):

    LoginPage(page).login(
        STANDARD_USER,
        PASSWORD
    )

    assert ProductsPage(page).cart_visible()