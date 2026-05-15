"""
Task 16 - Selenium Automation using Python, POM, Explicit Wait, Expected Conditions and Pytest

Description:
1. Open the World Population Clock website
2. Extract the live population count continuously
3. Print the count in terminal until user presses CTRL + C
4. Use XPath only

 Ritik Kumar Singh
"""

import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class WorldPopulationPage:
    """
    Page Object Model class for World Population Page
    """

    # URL of the website
    URL = "https://www.theworldcounts.com/challenges/planet-earth/state-of-the-planet/world-population-clock-live"

    # XPath locator for population count
    POPULATION_COUNT_XPATH = "//div[@class='counter-ticker is-size-2-mobile']"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def open_website(self):
        """
        Open the target website
        """
        self.driver.get(self.URL)
        self.driver.maximize_window()

    def get_population_count(self):
        """
        Fetch the live population count using explicit wait
        """
        population_element = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, self.POPULATION_COUNT_XPATH)
            )
        )
        return population_element.text


@pytest.fixture(scope="module")
def setup_driver():
    """
    Pytest fixture for browser setup and teardown
    """
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()


def test_live_population_counter(setup_driver):
    """
    Pytest test function to print live population count
    until user presses CTRL + C
    """

    driver = setup_driver

    # Create Page Object
    population_page = WorldPopulationPage(driver)

    # Open website
    population_page.open_website()

    print("\nLive Population Counter Started...")
    print("Press CTRL + C to stop execution.\n")

    try:
        while True:
            # Fetch population count
            population_count = population_page.get_population_count()

            # Print population count in terminal
            print(f"Current World Population: {population_count}")

            # Wait before refreshing data
            time.sleep(2)

    except KeyboardInterrupt:
        print("\nExecution stopped by user.")
