import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage


@pytest.fixture(scope="function")
def browser_page():

    with sync_playwright() as playwright:

        browser = playwright.chromium.launch(
            headless=False
        )

        page = browser.new_page()

        yield page

        browser.close()


def test_successful_login(browser_page):

    login = LoginPage(browser_page)

    login.open_portal()

    login.login("ritik740tomer@gmail.com", "Ritik740juhi@")

    assert "dashboard" in browser_page.url.lower()


def test_unsuccessful_login(browser_page):

    login = LoginPage(browser_page)

    login.open_portal()

    login.login("wronguser", "wrongpassword")

    error_message = browser_page.locator("text=Invalid credentials")

    assert error_message.is_visible()


def test_validate_username_input(browser_page):

    login = LoginPage(browser_page)

    login.open_portal()

    assert browser_page.locator(login.username_input).is_visible()


def test_validate_password_input(browser_page):

    login = LoginPage(browser_page)

    login.open_portal()

    assert browser_page.locator(login.password_input).is_visible()


def test_validate_submit_button(browser_page):

    login = LoginPage(browser_page)

    login.open_portal()

    assert browser_page.locator(login.login_button).is_enabled()


def test_validate_logout_functionality(browser_page):

    login = LoginPage(browser_page)

    login.open_portal()

    login.login("Admin", "admin123")

    login.logout()

    assert "login" in browser_page.url.lower()