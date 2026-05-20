import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utilities.read_config import ReadConfig


@pytest.fixture()
def driver():
    browser = ReadConfig.get_browser()

    if browser.lower() == 'chrome':
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )

    driver.maximize_window()
    driver.implicitly_wait(10)

    yield driver

    driver.quit()

.logout_button)