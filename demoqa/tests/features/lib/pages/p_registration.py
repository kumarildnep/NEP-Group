from lib.pages.p_properties import BaseProperties


class Registration(BaseProperties):

    def __init__(self, browser, *args, **kwargs):
        BaseProperties.__init__(self, browser)
        self.browser = browser