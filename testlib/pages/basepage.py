# -*- coding: utf-8 -*-

from driver import Driver
# from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import logging

class BasePage(Driver):
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time_out=10):
        try:
            wait = WebDriverWait(self.driver, time_out)
            element = wait.until(
                EC.visibility_of_element_located((locator))
            )
            return element
        #     element = wait.until(
        #         EC.visibility_of_element_located((locator))
        #     )
        #     return element
        except Exception:
            raise Exception("Element by \"{0}\" with the value \"{1}\" cannot be found.".format(locator[0], locator[1]))


    def find_children(self, parent):
        children = parent.find_elements_by_xpath(".//*")
        return children