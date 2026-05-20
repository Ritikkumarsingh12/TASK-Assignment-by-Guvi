from utilities.driver_setup import get_driver
from utilities.config import BASE_URL


def test_home_url_accessible():
    driver = get_driver()

    driver.get(BASE_URL)

    assert "orangehrm" in driver.title.lower()

    driver.quit()