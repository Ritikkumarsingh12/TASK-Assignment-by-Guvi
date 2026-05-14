from behave import given, when, then
from pages.login_page import LoginPage

@given("User launches OrangeHRM portal")
def launch_portal(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    context.login_page = LoginPage(context.driver)

@when("User enters valid username and password")
def valid_login(context):
    context.login_page.login("Admin", "admin123")

@when("User enters invalid username and password")
def invalid_login(context):
    context.login_page.login("Admin", "wrongpass")

@when("User clicks login button")
def click_login(context):
    pass

@then("User should login successfully")
def verify_success(context):
    assert context.login_page.is_dashboard_displayed()

@then("Error message should be displayed")
def verify_error(context):
    assert context.login_page.is_error_displayed()

@then("User should logout successfully")
def logout_user(context):
    context.login_page.logout()