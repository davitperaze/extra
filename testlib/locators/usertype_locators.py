from selenium.webdriver.common.by import By

class UsertypeLocators():
    BACK_BUTTON = (By.XPATH, '/html/body/app-root/app-sidebar/div[2]/app-sign-up-page/app-sign-up-type/div/div')
    USER_TYPE_TITLE = (By.XPATH, '/html/body/app-root/app-sidebar/div[2]/app-sign-up-page/app-sign-up-type/div/h3')
    USER_TYPE_NORMAL = (By.XPATH, '/html/body/app-root/app-sidebar/div[2]/app-sign-up-page/app-sign-up-type/div/ul/li')
