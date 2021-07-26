from driver import Driver
from testlib.pages.basepage import BasePage as BP
from testlib.locators.register_locators import RegisterLocators as RL
from testlib.locators.login_locators import LoginLocators as LL

import sys

class RegisterFormPage(BP):
    def __init__(self):
        pass

    def close_button(self):
        logo = BP.find_element(self, LL.CLOSE)
        return logo

    def back_button(self):
        back_button = BP.find_element(self, RL.BACK_BUTTON)
        return back_button

    def form_header(self):
        form_header = BP.find_element(self, RL.FORM_TITLE)
        return form_header

    def name_input(self):
        name_input = BP.find_element(self, RL.NAME_INPUT)
        return name_input

    def name_label(self):
        name_label = BP.find_element(self, RL.NAME_LABEL)
        return name_label

    def last_name_input(self):
        last_name_input = BP.find_element(self, RL.LASTNAME_INPUT)
        return last_name_input
    
    def last_name_label(self):
        last_name_label = BP.find_element(self, RL.LASTNAME_LABEL)
        return last_name_label

    def email_input(self):
        email_input = BP.find_element(self, RL.EMAIL_INPUT)
        return email_input

    def email_label(self):
        email_label = BP.find_element(self, RL.EMAIL_LABEL)
        return email_label

    def day_input(self):
        day_input = BP.find_element(self, RL.DAY_INPUT)
        return day_input

    def day_label(self):
        day_label = BP.find_element(self, RL.DAY_LABEL)
        return day_label

    def day_list(self):
        day_list = BP.find_element(self, RL.DAY_LIST)
        return day_list

    def day_ch(self):
        day_ch = BP.find_children(self, self.day_list())
        return day_ch

    def day_val(self):
        day_val = BP.find_element(self, RL.DAY_VAL)
        return day_val

    def month_input(self):
        month_input = BP.find_element(self, RL.MONTH_INPUT)
        return month_input

    def month_label(self):
        month_label = BP.find_element(self, RL.MONTH_LABEL)
        return month_label

    def month_list(self):
        month_list = BP.find_element(self, RL.MONTH_LIST)
        return month_list

    def month_ch(self):
        month_ch = BP.find_children(self, self.month_list())
        return month_ch

    def month_val(self):
        month_val = BP.find_element(self, RL.MONTH_VAL)
        return month_val

    def year_input(self):
        year_input = BP.find_element(self, RL.YEAR_INPUT)
        return year_input

    def year_label(self):
        year_label = BP.find_element(self, RL.YEAR_LABEL)
        return year_label

    def year_list(self):
        year_list = BP.find_element(self, RL.YEAR_LIST)
        return year_list

    def year_ch(self):
        year_ch = BP.find_children(self, self.year_list())
        return year_ch

    def year_val(self):
        year_val = BP.find_element(self, RL.YEAR_VAL)
        return year_val

    def register_button(self):
        register_button = BP.find_element(self, RL.REGISTER_BUTTON)
        return register_button

    def get_active_element(self):
        active = Driver.driver.switch_to.active_element
        return active
