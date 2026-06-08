from pages.login_page import LoginPage
from utils.config import *

def test_login_predefined_users(page):

    login = LoginPage(page)

    users = [
        STANDARD_USER,
        PROBLEM_USER,
        PERFORMANCE_USER
    ]

    for user in users:

        page.goto(BASE_URL)

        login.login(user, PASSWORD)

        assert "inventory" in page.url