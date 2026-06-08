from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from utils.config import *

def test_logout(page):

    login = LoginPage(page)

    login.login(STANDARD_USER, PASSWORD)

    products = ProductsPage(page)

    products.logout()

    assert login.is_login_page_displayed()