from lib.pages.p_registration import Registration


class Search(Registration):

    def __init__(self, browser, *args, **kwargs):
        Registration.__init__(self, browser)
        self.browser = browser