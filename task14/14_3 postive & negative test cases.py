import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


# 🔐 VALID CREDENTIALS (Replace with your real credentials)
VALID_USERNAME = "your_email@gmail.com"
VALID_PASSWORD = "your_password"

INVALID_USERNAME = "wrong@gmail.com"
INVALID_PASSWORD = "wrong123"


def test_successful_login(setup):
    login = LoginPage(setup)
    login.login(VALID_USERNAME, VALID_PASSWORD)

    assert "zen" in setup.current_url.lower()


def test_unsuccessful_login(setup):
    login = LoginPage(setup)
    login.login(INVALID_USERNAME, INVALID_PASSWORD)

    assert "invalid" in login.get_error_message().lower()


def test_validate_input_boxes(setup):
    login = LoginPage(setup)

    assert setup.find_element(*login.username_input).is_displayed()
    assert setup.find_element(*login.password_input).is_displayed()


def test_validate_submit_button(setup):
    login = LoginPage(setup)

    assert setup.find_element(*login.login_button).is_enabled()


def test_logout_functionality(setup):
    login = LoginPage(setup)
    login.login(VALID_USERNAME, VALID_PASSWORD)

    dashboard = DashboardPage(setup)
    dashboard.logout()

    assert "sign-in" in setup.current_url.lower()
