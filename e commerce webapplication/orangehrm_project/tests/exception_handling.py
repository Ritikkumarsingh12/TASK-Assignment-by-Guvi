try:
    element = driver.find_element(By.NAME, "username")
    element.send_keys("Admin")
except Exception as e:
    print("Element not found:", e)