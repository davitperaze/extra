from selenium.webdriver.common.by import By

class UsertypeLocators():
    BACK_BUTTON = (By.XPATH, '/html/body/app-root/app-sidebar/div[2]/app-sign-up-page/app-sign-user-info/div/div')
    FORM_TITLE = (By.XPATH, '/html/body/app-root/app-sidebar/div[2]/app-sign-up-page/app-sign-user-info/div/h3')
    
    NAME_INPUT = (By.XPATH, '/html/body/app-root/app-sidebar/div[2]/app-sign-up-page/app-sign-user-info/div/form/div[1]/div[1]/app-new-input/input')
    NAME_LABEL = (By.XPATH, '/html/body/app-root/app-sidebar/div[2]/app-sign-up-page/app-sign-user-info/div/form/div[1]/div[1]/app-new-input/label')

    LASTNAME_INPUT = (By.XPATH, '/html/body/app-root/app-sidebar/div[2]/app-sign-up-page/app-sign-user-info/div/form/div[1]/div[2]/app-new-input/input')
    LASTNAME_LABEL = (By.XPATH, '/html/body/app-root/app-sidebar/div[2]/app-sign-up-page/app-sign-user-info/div/form/div[1]/div[2]/app-new-input/label')

    EMAIL_INPUT = (By.XPATH, '/html/body/app-root/app-sidebar/div[2]/app-sign-up-page/app-sign-user-info/div/form/div[2]/app-new-input/input')
    EMAIL_LABEL = (By.XPATH, '/html/body/app-root/app-sidebar/div[2]/app-sign-up-page/app-sign-user-info/div/form/div[2]/app-new-input/label')

    DAY = (By.XPATH, '/html/body/app-root/app-sidebar/div[2]/app-sign-up-page/app-sign-user-info/div/form/div[3]/div/app-new-date-picker/form/div/div/div[1]')
    MONTH = (By.XPATH, '/html/body/app-root/app-sidebar/div[2]/app-sign-up-page/app-sign-user-info/div/form/div[3]/div/app-new-date-picker/form/div/div/div[2]')
    YEAR = (By.XPATH, '/html/body/app-root/app-sidebar/div[2]/app-sign-up-page/app-sign-user-info/div/form/div[3]/div/app-new-date-picker/form/div/div/div[3]')

    REGISTER_BUTTON = (By.XPATH, '/html/body/app-root/app-sidebar/div[2]/app-sign-up-page/app-sign-user-info/div/form/div[4]/button')