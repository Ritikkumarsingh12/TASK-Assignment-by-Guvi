import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# ---------------- FIXTURE SETUP ----------------

@pytest.fixture
def driver():
    """
    This fixture initializes and quits the browser.
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.get("https://jqueryui.com/droppable/")
    yield driver
    driver.quit()


# ---------------- HELPER FUNCTION ----------------

def switch_to_iframe(driver):
    """
    Switch into iframe where drag-drop elements exist.
    """
    iframe = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "demo-frame"))
    )
    driver.switch_to.frame(iframe)


# ---------------- POSITIVE TEST CASE ----------------

def test_drag_and_drop_positive(driver):
    """
    Positive Test Case:
    Drag white box into yellow box and verify success.
    """
    switch_to_iframe(driver)

    source = driver.find_element(By.ID, "draggable")
    target = driver.find_element(By.ID, "droppable")

    actions = ActionChains(driver)
    actions.drag_and_drop(source, target).perform()

    result_text = target.text

    assert "Dropped!" in result_text


# ---------------- NEGATIVE TEST CASE ----------------

def test_drag_and_drop_negative(driver):
    """
    Negative Test Case:
    Do NOT perform drag and drop and verify box is NOT dropped.
    """
    switch_to_iframe(driver)

    target = driver.find_element(By.ID, "droppable")

    result_text = target.text

    assert "Dropped!" not in result_text
