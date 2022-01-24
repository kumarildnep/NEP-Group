from selenium.webdriver.common.by import By


class RegistrationLocators():

    # Scenario: Verify user successful registration
    newUserButton = (By.XPATH, '//button[@id="newUser"]')
    # iframeCaptcha = 'recaptcha-token'
    # captchaCheckbox = (By.XPATH, '//div[@class="recaptcha-checkbox-border"]')
    firstNameInput = (By.XPATH, '//input[@id="firstname"]')
    lastNameInput = (By.XPATH, '//input[@id="lastname"]')
    userNameInput = (By.XPATH, '//input[@id="userName"]')
    passwordInput = (By.XPATH, '//input[@id="password"]')
    registerButton = (By.XPATH, '//button[@id="register"][text()="Register"]')
    joinNowButton = (By.XPATH, '//div[@class="home-banner"]//img[@class="banner-image"]')