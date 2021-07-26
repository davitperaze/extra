# -*- coding: utf-8 -*-

from selenium import webdriver as wb
from selenium.webdriver.chrome.options import Options


class Driver:
    options = Options()
    # options.add_argument("--headless")
    driver = wb.Chrome("chromedriver", options=options)

    driver.maximize_window()
    driver.get("https://extra.ge")
    driver.implicitly_wait(10)

    print("Driver initialized. {a}".format(a=driver.title))