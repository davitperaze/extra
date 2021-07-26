from driver import Driver
from testlib.pages.basepage import BasePage as BP
from testlib.locators.otp_locators import OtpLocators as OTPL

import sys

class OtpFormPage(BP):
    def __init__(self):
        pass

    def close_button(self):
        logo = BP.find_element(self, OTPL.CLOSE)
        return logo

    def back_button(self):
        back_button = BP.find_element(self, OTPL.BACK_BUTTON)
        return back_button

    def form_header(self):
        form_header = BP.find_element(self, OTPL.FORM_TITLE)
        return form_header

    def message(self):
        message = BP.find_element(self, OTPL.MESSAGE)
        return message

    def otp_input(self):
        otp_input = BP.find_element(self, OTPL.OTP_INPUT)
        return otp_input

    def otp_label(self):
        otp_label = BP.find_element(self, OTPL.OTP_LABEL)
        return otp_label

    def otp_resend(self):
        otp_resend = BP.find_element(self, OTPL.OTP_RESEND)
        return otp_resend

    def otp_submit(self):
        otp_submit = BP.find_element(self, OTPL.OTP_SUBMIT)
        return otp_submit