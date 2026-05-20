from selenium.webdriver.common.by import By
from utilities.driver_setup import get_driver
from utilities.config import BASE_URL


def test_login_fields_visible():
    driver = get_driver()

    driver.get(BASE_URL)

    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")

    assert username.is_displayed()
    assert password.is_displayed()

    driver.quit()