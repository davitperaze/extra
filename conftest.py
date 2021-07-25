# -*- coding: utf-8 -*-
from driver import Driver


def pytest_sessionfinish(session, exitstatus):
    Driver.driver.quit()
