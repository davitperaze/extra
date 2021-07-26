from selenium.webdriver.common.by import By

class PasswordLocators():
    CLOSE = (By.XPATH, '/html/body/app-root/app-sidebar/div[2]/div/button')
    FORM_TITLE = (By.XPATH, '/html/body/app-root/app-sidebar/div[2]/app-sign-up-page/app-sign-up-password/div/h3')
    
    PASSWORD = (By.XPATH, '/html/body/app-root/app-sidebar/div[2]/app-sign-up-page/app-sign-up-password/div/form/div[1]/app-new-input/input')
    PASSWORD_LABEL = (By.XPATH, '/html/body/app-root/app-sidebar/div[2]/app-sign-up-page/app-sign-up-password/div/form/div[1]/app-new-input/label')
    PASSWORD_VIEW = (By.XPATH, '/html/body/app-root/app-sidebar/div[2]/app-sign-up-page/app-sign-up-password/div/form/div[1]/app-new-input/div')

    REPEAT_PASSWORD = (By.XPATH, '/html/body/app-root/app-sidebar/div[2]/app-sign-up-page/app-sign-up-password/div/form/div[2]/app-new-input/input')
    REPEAT_PASSWORD_LABEL = (By.XPATH, '/html/body/app-root/app-sidebar/div[2]/app-sign-up-page/app-sign-up-password/div/form/div[2]/app-new-input/label')
    REPEAT_PASSWORD_VIEW = (By.XPATH, '/html/body/app-root/app-sidebar/div[2]/app-sign-up-page/app-sign-up-password/div/form/div[2]/app-new-input/div')

    TOC = (By.XPATH, '/html/body/app-root/app-sidebar/div[2]/app-sign-up-page/app-sign-up-password/div/form/div[3]/div')
    TOC_LABEL = (By.XPATH, '/html/body/app-root/app-sidebar/div[2]/app-sign-up-page/app-sign-up-password/div/form/div[3]/div/label')
    TOC_LINK = (By.XPATH, '/html/body/app-root/app-sidebar/div[2]/app-sign-up-page/app-sign-up-password/div/form/div[3]/div/a')

    SUBMIT = (By.XPATH, '/html/body/app-root/app-sidebar/div[2]/app-sign-up-page/app-sign-up-password/div/form/div[4]/button')