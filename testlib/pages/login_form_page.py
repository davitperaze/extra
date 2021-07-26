from testlib.pages.basepage import BasePage as BP
from testlib.locators.login_locators import LoginLocators as LC

import sys

class LoginFormPage(BP):
    def __init__(self):
        pass

    def close_button(self):
        logo = BP.find_element(self, LC.CLOSE)
        return logo

    def form_header(self):
        form_header = BP.find_element(self, LC.FORM_HEADER)
        return form_header

    def register_link(self):
        register_link = BP.find_element(self, LC.NEW_HERE_LINK)
        return register_link