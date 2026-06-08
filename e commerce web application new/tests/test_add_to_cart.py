from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from utils.config import *


def test_random_product_selection(page):
    LoginPage(page).login(
        STANDARD_USER,
        PASSWORD
    )

    products = ProductsPage(page)

    names = products.select_random_products(4)

    print(names)

    assert len(names) == 4


t_visible()