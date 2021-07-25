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
        logging.info("I'm here!")
        wait = WebDriverWait(self.driver, time_out)
        element = wait.until(
            EC.visibility_of_element_located((locator))
        )
        return element
        # try:
        #     element = wait.until(
        #         EC.visibility_of_element_located((locator))
        #     )
        #     return element
        # except Exception:
        #     raise Exception("Element by {how} with the value {what} cannot be found.")