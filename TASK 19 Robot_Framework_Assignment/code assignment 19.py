from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# ---------------------------------------------------------
# RobotSpareBinIndustries Login Automation using Python
# ---------------------------------------------------------
# This script performs:
# 1. Open Browser
# 2. Navigate to Application
# 3. Login with Valid Credentials
# 4. Verify Successful Login
# 5. Logout
# 6. Close Browser
# ---------------------------------------------------------

# Application URL
URL = "https://robotsparebinindustries.com/"

# Login Credentials
USERNAME = "Ritik740tomer@gmail.com"
PASSWORD = "Password@123"

# ---------------------------------------------------------
# Configure Chrome Browser
# ---------------------------------------------------------
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

# Initialize Chrome Driver
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=chrome_options
)

# ---------------------------------------------------------
# Open Application
# ---------------------------------------------------------
print("Opening Browser...")

driver.get(URL)

time.sleep(2)

# ---------------------------------------------------------
# Login Function
# ---------------------------------------------------------
def login():
    print("Entering Login Credentials...")

    # Enter Username
    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys(USERNAME)

    # Enter Password
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys(PASSWORD)

    # Click Login Button
    login_button = driver.find_element(
        By.XPATH,
        "//button[contains(text(),'Log in')]"
    )
    login_button.click()

    time.sleep(3)

# ---------------------------------------------------------
# Verify Login
# ---------------------------------------------------------
def verify_login():
    print("Verifying Successful Login...")

    try:
        dashboard_text = driver.find_element(
            By.XPATH,
            "//h2[contains(text(),'Orders overview')]"
        )

        if dashboard_text.is_displayed():
            print("LOGIN SUCCESSFUL")
        else:
            print("LOGIN FAILED")

    except Exception as e:
        print("Verification Failed")
        print(e)

# ---------------------------------------------------------
# Logout Function
# ---------------------------------------------------------
def logout():
    print("Logging Out...")

    logout_button = driver.find_element(
        By.XPATH,
        "//button[contains(text(),'Log out')]"
    )

    logout_button.click()

    time.sleep(2)

# ---------------------------------------------------------
# Execute Test Flow
# ---------------------------------------------------------
try:
    login()
    verify_login()
    logout()

except Exception as e:
    print("Test Execution Failed")
    print(e)

finally:
    # -----------------------------------------------------
    # Close Browser
    # -----------------------------------------------------
    print("Closing Browser...")
    driver.quit()

    print("Test Execution Completed")