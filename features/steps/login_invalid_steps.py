from behave import when, then
from pages.Loginpage import LoginPage


@when('enters invalid email "{email}" and password "{password}"')
def step_impl(context, email, password):
    login = LoginPage(context.driver)
    login.login(email, password)


@then('"{expected_text}" should be displayed')
def step_impl(context, expected_text):
    login = LoginPage(context.driver)
    actual_text = login.get_error_message()
    assert expected_text in actual_text
