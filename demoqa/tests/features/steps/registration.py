import time

from behave import *
from lib.locators.l_registration import RegistrationLocators as RL
from lib.pages.p_registration import Registration


# Scenario: Verify user successful registration

@Given(u'user navigate to DemoQA website')
def step_impl(context):
    ob_RL = Registration(context.browser)
    ob_RL.wait_document_ready_state()


@When(u'user clicks on New User button')
def step_impl(context):
    ob_RL = Registration(context.browser)
    ob_RL.click_element(RL.newUserButton)


@When(u'user provides "{firstName}","{lastName}","{userName}" and "{password}"')
def step_impl(context, firstName, lastName, userName, password):
    ob_RL = Registration(context.browser)
    ob_RL.set_element_value(RL.firstNameInput, ob_RL.property(firstName))
    ob_RL.set_element_value(RL.lastNameInput, ob_RL.property(lastName))
    ob_RL.set_element_value(RL.userNameInput, ob_RL.property(userName))
    ob_RL.set_element_value(RL.passwordInput, ob_RL.property(password))
    # ob_RL.set_focus_on_iframe()
    # ob_RL.click_element(RL.captchaCheckbox)


@When(u'user clicks on Register button')
def step_impl(context):
    ob_RL = Registration(context.browser)
    ob_RL.press_enterkey_at_element(RL.registerButton)

# @Then(u'it successfully register the user')

# It is not possible to automate the Captcha and that is the whole idea
# to prevent hackers accessing web applications via using bots.

# There are three efficient ways of handling Captcha in selenium
# * By disabling the Captcha in the testing environment
# * Adding a hook to click the Captcha checkbox
# * By adding a delay to the Webdriver and manually solve Captcha while testing

# I have tried using chromeoptions at environment.py file to disable the extensions
# at register page and written a script to click the captcha checkbox by identifying
# the element in the iframe but the script always failed in locating the iframe check box