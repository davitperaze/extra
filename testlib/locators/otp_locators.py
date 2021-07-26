from selenium.webdriver.common.by import By

class OtpLocators():
    CLOSE = (By.XPATH, '/html/body/app-root/app-sidebar/div[2]/div/button')
    BACK_BUTTON = (By.XPATH, '/html/body/app-root/app-sidebar/div[2]/app-sign-up-page/app-sign-up-validate/div/div[1]')
    FORM_TITLE = (By.XPATH, '/html/body/app-root/app-sidebar/div[2]/app-sign-up-page/app-sign-up-validate/div/h3')
    
    MESSAGE = (By.XPATH, '/html/body/app-root/app-sidebar/div[2]/app-sign-up-page/app-sign-up-validate/div/p')

    OTP_INPUT = (By.XPATH, '/html/body/app-root/app-sidebar/div[2]/app-sign-up-page/app-sign-up-validate/div/div[2]/div/div/app-otp-validate/div/form/div[1]/app-new-input/input')
    OTP_LABEL = (By.XPATH, '/html/body/app-root/app-sidebar/div[2]/app-sign-up-page/app-sign-up-validate/div/div[2]/div/div/app-otp-validate/div/form/div[1]/app-new-input/label')
    OTP_RESEND = (By.XPATH, '/html/body/app-root/app-sidebar/div[2]/app-sign-up-page/app-sign-up-validate/div/div[2]/div/div/app-otp-validate/div/div/button')

    OTP_SUBMIT = (By.XPATH, '/html/body/app-root/app-sidebar/div[2]/app-sign-up-page/app-sign-up-validate/div/div[2]/div/div/app-otp-validate/div/form/div[2]/button')