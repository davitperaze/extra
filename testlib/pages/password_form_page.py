from driver import Driver
from testlib.pages.basepage import BasePage as BP
from testlib.locators.password_locators import PasswordLocators as PFL
import random, string

import sys

class PasswordFormPage(BP):
    def __init__(self):
        pass

    def close_button(self):
        logo = BP.find_element(self, PFL.CLOSE)
        return logo

    

    def form_header(self):
        form_header = BP.find_element(self, PFL.FORM_TITLE)
        return form_header

    def password_input(self):
        password_input = BP.find_element(self, PFL.PASSWORD)
        return password_input
 
    def password_label(self):
        password_label = BP.find_element(self, PFL.PASSWORD_LABEL)
        return password_label

    def password_view(self):
        password_view = BP.find_element(self, PFL.PASSWORD_VIEW)
        return password_view

    def repeat_password(self):
        repeat_password = BP.find_element(self, PFL.REPEAT_PASSWORD)
        return repeat_password

    def repeat_password_label(self):
        repeat_password_label = BP.find_element(self, PFL.REPEAT_PASSWORD_LABEL)
        return repeat_password_label

    def repeat_password_view(self):
        repeat_password_view = BP.find_element(self, PFL.REPEAT_PASSWORD_VIEW)
        return repeat_password_view

    def toc(self):
        toc = BP.find_element(self, PFL.TOC)
        return toc

    def toc_label(self):
        toc_label = BP.find_element(self, PFL.TOC_LABEL)
        return toc_label

    def toc_link(self):
        toc_link = BP.find_element(self, PFL.TOC_LINK)
        return toc_link


    def password_submit(self):
        password_submit = BP.find_element(self, PFL.SUBMIT)
        return password_submit

    def gen_password(self):
        password = ''.join(random.choice(string.printable) for i in range(12))
        return password