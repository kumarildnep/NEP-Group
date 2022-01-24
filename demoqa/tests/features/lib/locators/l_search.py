from selenium.webdriver.common.by import By
from lib.locators.l_registration import RegistrationLocators


class SearchLocators(RegistrationLocators):

    # Scenario: Book Search
    gotoBookStoreButton = (By.XPATH, '//button[@id="gotoStore"]')
    searchBookInput = (By.XPATH, '//input[@id="searchBox"]')
    searchBookLink = (By.XPATH, '//span//a[contains(@href, "books")]')

    # Scenario: Verify search book details
    bookISBN = (By.XPATH, '//div[@id="ISBN-wrapper"]//label[@id="ISBN-label"]')
