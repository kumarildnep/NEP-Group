from selenium.webdriver.common.by import By
from lib.locators.l_registration import RegistrationLocators


class AuthenticationLocators(RegistrationLocators):

    # Scenario: Verify user authentication
    loginButton = (By.XPATH, '//button[@id="login"]')
    logoutButton = (By.XPATH, '//button[text()="Log out"]')

    # Scenario: Verify authentication failure
    loginErrorMsg = (By.XPATH, '//p[text()="Invalid username or password!"]')