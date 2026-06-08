class CheckoutPage:

    def __init__(self, page):
        self.page = page

    def enter_user_info(self, fname, lname, zip_code):

        self.page.fill("#first-name", fname)
        self.page.fill("#last-name", lname)
        self.page.fill("#postal-code", zip_code)

        self.page.click("#continue")

    def finish_order(self):

        self.page.screenshot(
            path="screenshots/order_summary.png"
        )

        self.page.click("#finish")

    def confirmation_message(self):

        return self.page.locator(
            ".complete-header"
        ).text_content()