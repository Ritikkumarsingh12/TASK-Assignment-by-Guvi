from selenium.webdriver.common.by import By
from utilities.driver_setup import get_driver
from utilities.config import BASE_URL, USERNAME, PASSWORD


def test_assign_leave():
    driver = get_driver()

    driver.get(BASE_URL)

    driver.find_element(By.NAME, "username").send_keys(USERNAME)
    driver.find_element(By.NAME, "password").send_keys(PASSWORD)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    driver.find_element(By.XPATH, "//*[text()='Leave']").click()

    assert "leave" in driver.current_url.lower()

    driver.quit()