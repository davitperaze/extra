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

    def categories(self):
        categories = BP.find_element(self, CL.CATEGORIES)
        return categories

    def search_bar(self):
        search_bar = BP.find_element(self, CL.SEARCHBAR)
        return search_bar

    def cart(self):
        cart = BP.find_element(self, CL.CART)
        return cart

    def check_user_button(self):
        user_button = BP.find_element(self, CL.USERDATA)
        return user_button

    def click_user_button(self):
        self.check_user_button().click()