from behave import *
from pages.Loginpage import LoginPage


@when('enters valid email "{email}" and password "{password}"')
def step_impl(context, email, password):
    login = LoginPage(context.driver)
    login.login(email, password)


@then('"{expected_text}" should be visible')
def step_impl(context, expected_text):
    login = LoginPage(context.driver)
    actual_text = login.get_login_message()
    assert expected_text in actual_text
