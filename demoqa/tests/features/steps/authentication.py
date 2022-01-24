import time

from behave import *
from lib.locators.l_authentication import AuthenticationLocators as AL
from lib.pages.p_authentication import Authentication


# Scenario: Verify user authentication

@Given(u'user navigates to login page')
def step_impl(context):
    context.execute_steps(u'given user navigate to DemoQA website')


@When(u'user enters valid "{userName}" and "{password}"')
def step_impl(context, userName, password):
    ob_AL = Authentication(context.browser)
    ob_AL.set_element_value(AL.userNameInput, ob_AL.property(userName))
    time.sleep(0.3)
    ob_AL.set_element_value(AL.passwordInput, ob_AL.property(password))
    time.sleep(0.3)


@When(u'user clicks on Login button')
def step_impl(context):
    ob_AL = Authentication(context.browser)
    ob_AL.click_element(AL.loginButton)


@Then(u'user successfully login')
def step_impl(context):
    ob_AL = Authentication(context.browser)
    ob_AL.check_element(AL.logoutButton)


# Scenario: Verify authentication failure

@When(u'user enters "{invalidUserName}" and "{incorrectPassword}"')
def step_impl(context, invalidUserName, incorrectPassword):
    ob_AL = Authentication(context.browser)
    ob_AL.set_element_value(AL.userNameInput, ob_AL.property(invalidUserName))
    time.sleep(0.3)
    ob_AL.set_element_value(AL.passwordInput, ob_AL.property(incorrectPassword))
    time.sleep(0.3)


@Then(u'user login is unsuccessful')
def step_impl(context):
    ob_AL = Authentication(context.browser)
    ob_AL.check_element(AL.loginErrorMsg)