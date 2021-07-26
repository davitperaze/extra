from driver import Driver
from testlib.pages.basepage import BasePage as BP
from testlib.locators.success_locators import SuccessLocators as SL

import sys

class SuccessPage(BP):
    def __init__(self):
        pass

    def close_button(self):
        close = BP.find_element(self, SL.CLOSE)
        return close

    def image(self):
        image = BP.find_element(self, SL.IMAGE)
        return image

    def header_text(self):
       header_text = BP.find_element(self, SL.CONG)
       return header_text

    def message(self):
        message = BP.find_element(self, SL.TEXT)
        return message

    def button(self):
        button = BP.find_element(self, SL.BUTTON)
        return button