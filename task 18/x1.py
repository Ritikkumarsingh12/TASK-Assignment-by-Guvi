from behave import given, when, then
from utils.driver_factory import get_driver
from pages.login_page import LoginPage
import time

@given('user launches the browser')
def step_impl(context):
    context.driver = get_driver()

@when('user opens the Zen portal')
def step_impl(context):
    context.driver.get("https://v2.zenclass.in/class")
    context.login_page = LoginPage(context.driver)

@when('user enters valid username and password')
def step_impl(context):
    context.login_page.enter_username("Ritik740tomer@gmail.com")
    context.login_page.enter_password("admin123")

@when('user enters invalid username and password')
def step_impl(context):
    context.login_page.enter_username("wrong ritik")
    context.login_page.enter_password("wrong")

@when('clicks on login button')
def step_impl(context):
    context.login_page.click_login()
    time.sleep(2)

@then('user should be logged in successfully')
def step_impl(context):
    assert context.login_page.is_login_success()

@then('login should fail')
def step_impl(context):
    assert "login" in context.driver.current_url

@then('user logs out')
def step_impl(context):
    context.login_page.click_logout()