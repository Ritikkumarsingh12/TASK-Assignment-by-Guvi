class LoginPage:

    def __init__(self, page):
        self.page = page

    def login(self, username, password):

        self.page.fill("#user-name", username)
        self.page.fill("#password", password)
        self.page.click("#login-button")

    def get_error_message(self):
        return self.page.locator("[data-test='error']").text_content()

    def is_login_page_displayed(self):
        return self.page.locator("#login-button").is_visible()