from testlib.pages.basepage import BasePage as BP
from testlib.locators.common_locators import CommonLocators as CL

import sys

class HomePage(BP):
    def __init__(self):
        pass

    def check_page_loaded(self):
        logo = BP.find_element(self, CL.LOGO)
        # print(logo.is_displayed())
        return logo

    def check_user_button(self):
        user_button = BP.find_element(self, CL.USERDATA)
        return user_button

    def click_user_button(self):
        self.check_user_button().click()