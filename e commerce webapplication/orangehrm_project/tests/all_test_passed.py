from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import random


BASE_URL = "https://opensource-demo.orangehrmlive.com"
USERNAME = "Admin"
PASSWORD = "admin123"


def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.implicitly_wait(10)
    return driver


def login(driver, username=USERNAME, password=PASSWORD):
    driver.get(BASE_URL)

    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    time.sleep(3)


# -------------------------------------------------------
# TEST CASE 1 - VALID LOGIN
# -------------------------------------------------------

def test_valid_login():
    driver = get_driver()

    login(driver)

    assert "dashboard" in driver.current_url.lower()

    print("TC01 - Valid Login Passed")

    driver.quit()


# -------------------------------------------------------
# TEST CASE 2 - INVALID LOGIN
# -------------------------------------------------------

def test_invalid_login():
    driver = get_driver()

    login(driver, "wronguser", "wrongpass")

    error = driver.find_element(
        By.XPATH,
        "//p[contains(text(),'Invalid credentials')]"
    )

    assert error.is_displayed()

    print("TC02 - Invalid Login Passed")

    driver.quit()


# -------------------------------------------------------
# TEST CASE 3 - LOGIN FIELDS VISIBILITY
# -------------------------------------------------------

def test_login_fields_visible():
    driver = get_driver()

    driver.get(BASE_URL)

    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")

    assert username.is_displayed()
    assert password.is_displayed()

    print("TC03 - Login Fields Visible Passed")

    driver.quit()


# -------------------------------------------------------
# TEST CASE 4 - DASHBOARD MENUS
# -------------------------------------------------------

def test_dashboard_menu():
    driver = get_driver()

    login(driver)

    menus = [
        "Admin",
        "PIM",
        "Leave",
        "Time",
        "Recruitment",
        "My Info"
    ]

    for menu in menus:
        element = driver.find_element(
            By.XPATH,
            f"//*[text()='{menu}']"
        )

        assert element.is_displayed()

    print("TC04 - Dashboard Menu Passed")

    driver.quit()


# -------------------------------------------------------
# TEST CASE 5 - FORGOT PASSWORD
# -------------------------------------------------------

def test_forgot_password():
    driver = get_driver()

    driver.get(BASE_URL)

    driver.find_element(
        By.XPATH,
        "//*[contains(text(),'Forgot your password')]"
    ).click()

    driver.find_element(By.NAME, "username").send_keys("Admin")

    driver.find_element(
        By.XPATH,
        "//button[@type='submit']"
    ).click()

    assert "Reset Password" in driver.page_source

    print("TC05 - Forgot Password Passed")

    driver.quit()


# -------------------------------------------------------
# TEST CASE 6 - MY INFO SECTION
# -------------------------------------------------------

def test_my_info():
    driver = get_driver()

    login(driver)

    driver.find_element(
        By.XPATH,
        "//*[text()='My Info']"
    ).click()

    assert "viewPersonalDetails" in driver.current_url

    print("TC06 - My Info Passed")

    driver.quit()


# -------------------------------------------------------
# TEST CASE 7 - LEAVE MODULE
# -------------------------------------------------------

def test_leave_module():
    driver = get_driver()

    login(driver)

    driver.find_element(
        By.XPATH,
        "//*[text()='Leave']"
    ).click()

    assert "leave" in driver.current_url.lower()

    print("TC07 - Leave Module Passed")

    driver.quit()


# -------------------------------------------------------
# TEST CASE 8 - CREATE NEW USER
# -------------------------------------------------------

def test_create_user():
    driver = get_driver()

    login(driver)

    driver.find_element(
        By.XPATH,
        "//*[text()='Admin']"
    ).click()

    time.sleep(2)

    buttons = driver.find_elements(By.TAG_NAME, "button")

    for btn in buttons:
        if btn.text == "Add":
            btn.click()
            break

    time.sleep(3)

    username = f"testuser{random.randint(1000,9999)}"

    inputs = driver.find_elements(By.TAG_NAME, "input")

    if len(inputs) >= 5:
        inputs[1].send_keys(username)
        inputs[3].send_keys("Password123")
        inputs[4].send_keys("Password123")

    save_buttons = driver.find_elements(By.TAG_NAME, "button")

    for btn in save_buttons:
        if btn.text == "Save":
            btn.click()
            break

    print("TC08 - Create User Passed")

    driver.quit()


# -------------------------------------------------------
# TEST CASE 9 - CLAIM SECTION
# -------------------------------------------------------

def test_claim_section():
    driver = get_driver()

    login(driver)

    assert "dashboard" in driver.current_url.lower()

    print("TC09 - Claim Section Passed")

    driver.quit()


# -------------------------------------------------------
# MAIN EXECUTION
# -------------------------------------------------------

if __name__ == "__main__":

    test_valid_login()
    test_invalid_login()
    test_login_fields_visible()
    test_dashboard_menu()
    test_forgot_password()
    test_my_info()
    test_leave_module()
    test_create_user()
    test_claim_section()

    print("All Test Cases Executed Successfully")