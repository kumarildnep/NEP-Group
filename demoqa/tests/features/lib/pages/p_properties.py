from lib.Base_Page_Object import Page


class BaseProperties(Page):

    def __init__(self, browser, *args, **kwargs):
        Page.__init__(self, browser)
        self.browser = browser

    def property(self, property):
        switcher = {
            'First Name': 'John',
            'Last Name': 'Klevin',
            'New User Name': 'AutoTest',
            'New Password': 'AS!@qw12',
            'User Name': 'TestU',
            'Password': '@1Az$@1Az$',
            'Invalid Username': 'Test123',
            'Incorrect Password': '@1Az$56Az$',
            'Search Key': 'Designing'
        }
        return switcher.get(property, "Invalid property")