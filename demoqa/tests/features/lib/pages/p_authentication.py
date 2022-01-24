from lib.pages.p_registration import Registration


class Authentication(Registration):

    def __init__(self, browser, *args, **kwargs):
        Registration.__init__(self, browser)
        self.browser = browser