from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utilities.read_config import ReadConfig


class TestLogin:

    def test_valid_login(self, driver):
        driver.get(ReadConfig.get_application_url())

        homepage = HomePage(driver)
        homepage.click_login()

        loginpage = LoginPage(driver)
        loginpage.login(
            ReadConfig.get_email(),
            ReadConfig.get_password()
        )

        dashboard = DashboardPage(driver)
        assert dashboard.is_dashboard_loaded()

    def test_invalid_login(self, driver):
        driver.get(ReadConfig.get_application_url())

        homepage = HomePage(driver)
        homepage.click_login()

        loginpage = LoginPage(driver)
        loginpage.login('invalid@gmail.com', 'wrongpassword')

        assert loginpage.is_error_displayed()


isible()