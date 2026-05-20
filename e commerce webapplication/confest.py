import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope=class)
def setup(request)
    Initializes the WebDriver instance and ensures proper cleanup after tests.
    options = webdriver.ChromeOptions()
    options.add_argument(--start-maximized)
    # Uncomment next line for headless execution
    # options.add_argument(--headless) 
    
    driver = webdriver.Chrome(options=options)
    driver.get(httpswww.saucedemo.com)
    
    # Pass driver to the calling test class
    request.cls.driver = driver
    
    yield driver
    
    # Ensure browser is properly closed after all test cases execute 
    driver.quit()