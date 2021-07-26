from testlib.pages.basepage import BasePage as BP
from testlib.locators.usertype_locators import UsertypeLocators as UTL

import sys

class UserTypePage(BP):
    def __init__(self):
        pass

    def back_button(self):
        back = BP.find_element(self, UTL.BACK_BUTTON)
        return back

    def header(self):
        header = BP.find_element(self, UTL.USER_TYPE_TITLE)
        return header

    def user_type(self):
        user_type = BP.find_element(self, UTL.USER_TYPE_NORMAL)
        return user_type