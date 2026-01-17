import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# ---------- FIXTURE ----------
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


# ---------- TEST CASE ----------
def test_dynamic_xpath_and_axes(driver):
    URL = "https://www.guvi.in"   # change only if needed
    driver.get(URL)

    wait = WebDriverWait(driver, 40)

    # wait until page fully loads
    wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

    # LOGIN button (stable xpath)
    login_button = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//*[contains(text(),'Login')]")
        )
    )

    # validation
    assert login_button.is_displayed()

    print("Login button found successfully")
