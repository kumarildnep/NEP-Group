from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class Page(object):
    """
    Base class containing reusable methods
    """
    def __init__(self, selenium_driver):
        self.driver = selenium_driver
        self.timeout = 20

    def find_element_presence(self, loc, timeout=20):
        try:
            self.element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(loc))
            return self.element
        except:
            raise NoSuchElementException

    def find_element(self, loc, timeout=20):
        try:
            self.element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(loc))
            return self.element
        except:
            raise NoSuchElementException

    def find_click_element(self, loc, timeout=20):
        try:
            self.element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(loc))
            return self.element
        except:
            raise NoSuchElementException

    def wait_document_ready_state(self):
        try:
            WebDriverWait(self.driver, 20).until(lambda w: self.driver.execute_script('return document.readyState')=='complete')
        except:
            raise TimeoutError('document.readyState not set to complete in the given time period')

    def clear_element_value(self, element):
        return self.find_element(element).clear()

    def click_element(self, element):
        return self.find_click_element(element).click()

    def click_element_link(self, element):
        return self.find_element(element).click()

    def set_element_value(self, element, value):
        self.clear_element_value(element)
        return self.find_element(element).send_keys(value)

    def press_enterkey_at_element(self, element):
        return self.find_element(element).send_keys(Keys.RETURN)

    def check_element(self,element):
        return self.find_element_presence(element)

    def get_element_text(self, element):
        return self.find_element(element).text

    # def set_focus_on_iframe(self, element):
    #     self.driver.switch_to.frame(element)

