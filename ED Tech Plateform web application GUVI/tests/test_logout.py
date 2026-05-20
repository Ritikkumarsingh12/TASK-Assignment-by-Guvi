from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utilities.read_config import ReadConfig


class TestLogout:

    def test_logout(self, driver):
        driver.get(ReadConfig.get_application_url())

        homepage = HomePage(driver)
        homepage.click_login()

        loginpage = LoginPage(driver)
        loginpage.login(
            ReadConfig.get_email(),
            ReadConfig.get_password()
        )

        dashboard = DashboardPage(driver)
        dashboard.logout()

        assert 'login' in driver.current_url.lower()


current_url.lower()