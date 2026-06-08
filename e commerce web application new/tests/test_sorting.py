from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from utils.config import *

def test_sorting(page):

    LoginPage(page).login(
        STANDARD_USER,
        PASSWORD
    )

    products = ProductsPage(page)

    products.sort_products("lohi")

    assert page.locator(
        ".inventory_item"
    ).count() > 0