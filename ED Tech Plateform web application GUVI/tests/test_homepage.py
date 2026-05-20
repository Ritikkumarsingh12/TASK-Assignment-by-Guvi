from utilities.read_config import ReadConfig

class TestHomepage:

    def test_validate_homepage_title(self, driver):
        driver.get(ReadConfig.get_application_url())
        assert "GUVI" in driver.title
