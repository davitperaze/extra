from selenium.webdriver.common.by import By

class SuccessLocators():
    CLOSE = (By.XPATH, '/html/body/app-root/app-sidebar/div[2]/div/button')
    IMAGE = (By.XPATH, '/html/body/app-root/app-sidebar/div[2]/app-sign-up-page/app-sign-up-success/div/figure/img')
    CONG = (By.XPATH, '/html/body/app-root/app-sidebar/div[2]/app-sign-up-page/app-sign-up-success/div/h3')
    TEXT = (By.XPATH, '/html/body/app-root/app-sidebar/div[2]/app-sign-up-page/app-sign-up-success/div/p')
    BUTTON = (By.XPATH, '/html/body/app-root/app-sidebar/div[2]/app-sign-up-page/app-sign-up-success/div/div/button')