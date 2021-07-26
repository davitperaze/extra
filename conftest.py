# -*- coding: utf-8 -*-
from driver import Driver
import time
import pytest
import allure
import sys
import os

from pluggy import HookspecMarker
hookspec = HookspecMarker("pytest")
CT = time.time()

def pytest_sessionfinish(session, exitstatus):
    Driver.driver.quit()
    if "--collect-only" not in sys.argv:
            os.popen("allure serve reports/allure")

def pytest_runtest_teardown(item):
    node = item.obj
    image_name = "./reports/images/" + str(CT) + ".png"
    image = Driver.driver.get_screenshot_as_file(image_name)

    allure.attach.file(
        image_name,
        name=node.__name__+"-step__screenshot",
        attachment_type=allure.attachment_type.PNG,
    )


@hookspec(firstresult=True)
def pytest_runtest_makereport(item):
    node = item.obj
    print("\nNow testing: "+node.__name__)
    img = "./reports/images/" + str(CT) + ".png"
    Driver.driver.get_screenshot_as_file(img)
