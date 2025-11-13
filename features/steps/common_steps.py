from behave import *
from pages.Home_page import HomePage


@given('user is on home page')
def step_impl(context):
    # Browser already opened in environment.py
    context.driver.get("https://automationexercise.com/")


@when('user clicks on Signup/Login link')
def step_impl(context):
    home = HomePage(context.driver)
    home.click_signup_login()
