from pages.home_page import HomePage
from utilities.read_config import ReadConfig

class TestNavigation:

    def test_login_navigation(self, driver):
        driver.get(ReadConfig.get_application_url())

        homepage = HomePage(driver)
        homepage.click_login()

        assert 'login' in driver.current_url.lower()

    def test_signup_navigation(self, driver):
        driver.get(ReadConfig.get_application_url())

        homepage = HomePage(driver)
        homepage.click_signup()

        assert 'register' in driver.current_url.lower()