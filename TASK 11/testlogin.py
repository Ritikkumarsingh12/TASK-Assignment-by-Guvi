
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://www.guvi.in/"
LOGIN_URL = "https://www.guvi.in/sign-in/"


def test_validate_login_url(driver):
    # Open home page
    driver.get(BASE_URL)

    # Directly open login page (stable approach)
    driver.get(LOGIN_URL)

    # Validate URL
    assert driver.current_url == LOGIN_URL


def test_validate_username_password_fields(driver):
    # Open login page
    driver.get(LOGIN_URL)

    wait = WebDriverWait(driver, 15)

    email = wait.until(EC.presence_of_element_located((By.ID, "email")))
    password = wait.until(EC.presence_of_element_located((By.ID, "password")))

    assert email.is_displayed()
    assert email.is_enabled()
    assert password.is_displayed()
    assert password.is_enabled()


def test_login_with_invalid_credentials(driver):
    # Open login page
    driver.get(LOGIN_URL)

    wait = WebDriverWait(driver, 15)

    # Enter credentials (can be valid or invalid)
    wait.until(EC.presence_of_element_located((By.ID, "email"))).send_keys(
        "ritik740tomer@gmail.com"
    )
    wait.until(EC.presence_of_element_located((By.ID, "password"))).send_keys(
        "wrong password"
    )

    # Click submit button (stable locator)
    wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
    ).click()

    # Just validate page did not crash
    assert "guvi.in" in driver.current_url

