from pages.login_page import LoginPage

def test_invalid_login(page):

    login = LoginPage(page)

    login.login("invalid", "invalid")

    assert "Username and password" in \
           login.get_error_message()