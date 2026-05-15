from playwright.sync_api import Page


class LoginPage:

    def __init__(self, page: Page):

        self.page = page

        # Zen Portal Locators
        self.username_input = "input[type='email']"
        self.password_input = "input[type='password']"
        self.login_button = "button[type='submit']"

        self.profile_icon = "div.user-profile"
        self.logout_button = "text=Logout"

    def open_portal(self):

        self.page.goto(
            "https://v2.zenclass.in/login"
        )

        # Explicit wait
        self.page.wait_for_selector(
            self.username_input,
            timeout=20000
        )

    def enter_username(self, username):

        self.page.fill(
            self.username_input,
            username
        )

    def enter_password(self, password):

        self.page.fill(
            self.password_input,
            password
        )

    def click_login(self):

        self.page.click(
            self.login_button
        )

    def login(self, username, password):

        self.enter_username(username)

        self.enter_password(password)

        self.click_login()

        self.page.wait_for_timeout(5000)

    def logout(self):

        self.page.click(self.profile_icon)

        self.page.wait_for_selector(
            self.logout_button,
            timeout=10000
        )

        self.page.click(self.logout_button)