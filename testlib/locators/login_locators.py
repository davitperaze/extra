from selenium.webdriver.common.by import By

class LoginLocators():
    CLOSE = (By.XPATH, '/html/body/app-root/app-sidebar/div[2]/div/button')
    FORM_HEADER = (By.XPATH, '/html/body/app-root/app-sidebar/div[2]/app-sign-in-page/div/h3')
    USERNAME_INPUT = (By.XPATH, '/html/body/app-root/app-sidebar/div[2]/app-sign-in-page/div/form/div[2]/app-new-input/input')
    USERNAME_LABEL = (By.XPATH, '/html/body/app-root/app-sidebar/div[2]/app-sign-in-page/div/form/div[2]/app-new-input/label')
    PASSWORD_INPUT = (By.XPATH, '/html/body/app-root/app-sidebar/div[2]/app-sign-in-page/div/form/div[3]/app-new-input/input')
    PASSWORD_LABEL = (By.XPATH, '/html/body/app-root/app-sidebar/div[2]/app-sign-in-page/div/form/div[3]/app-new-input/label')
    PASSWORD_VIEW = (By.XPATH, '/html/body/app-root/app-sidebar/div[2]/app-sign-in-page/div/form/div[3]/app-new-input/div')
    FORGOT_PASSWORD_TEXT = (By.XPATH, '/html/body/app-root/app-sidebar/div[2]/app-sign-in-page/div/form/div[4]/p[1]')
    FORGOT_PASSWORD_LINK = (By.XPATH, '/html/body/app-root/app-sidebar/div[2]/app-sign-in-page/div/form/div[4]/p[1]/span')
    NEW_HERE_TEXT = (By.XPATH, '/html/body/app-root/app-sidebar/div[2]/app-sign-in-page/div/form/div[4]/p[2]')
    NEW_HERE_LINK = (By.XPATH, '/html/body/app-root/app-sidebar/div[2]/app-sign-in-page/div/form/div[4]/p[2]/span')
    LOGIN_BUTTON = (By.XPATH, '/html/body/app-root/app-sidebar/div[2]/app-sign-in-page/div/form/div[5]/button')
    FB_BUTTON = (By.XPATH, '/html/body/app-root/app-sidebar/div[2]/app-sign-in-page/div/form/div[7]/button[1]')
    GOOGLE_BUTTON = (By.XPATH, '/html/body/app-root/app-sidebar/div[2]/app-sign-in-page/div/form/div[7]/button[2]')

    