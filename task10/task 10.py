

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


def login_to_saucedemo(driver):
    """
    Logs into the SauceDemo website using valid credentials
    """
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    time.sleep(2)


def fetch_webpage_details(driver):
    """
    Fetch title, URL and save page source to text file
    """
    title = driver.title
    current_url = driver.current_url

    print("Page Title:", title)
    print("Current URL:", current_url)

    # Save page source to text file
    with open("Webpage_task_11.txt", "w", encoding="utf-8") as file:
        file.write(driver.page_source)


def main():
    """
    Main function to execute Selenium automation
    """
    service = Service()
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()

    login_to_saucedemo(driver)
    fetch_webpage_details(driver)

    driver.quit()


if __name__ == "__main__":
    main()
