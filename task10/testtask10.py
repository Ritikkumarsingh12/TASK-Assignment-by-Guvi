import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


@pytest.fixture
def driver():
    service = Service()
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_positive_login(driver):
    """
    Positive test case: Valid login
    """
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    time.sleep(2)

    # Title check
    assert driver.title == "Swag Labs"

    # Dashboard URL check
    assert "inventory.html" in driver.current_url


def test_negative_login(driver):
    """
    Negative test case: Invalid login
    """
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("wrong_user")
    driver.find_element(By.ID, "password").send_keys("wrong_password")
    driver.find_element(By.ID, "login-button").click()

    time.sleep(2)

    error_message = driver.find_element(By.XPATH, "//h3").text
    assert "Username and password do not match" in error_message
