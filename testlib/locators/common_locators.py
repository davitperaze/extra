from selenium.webdriver.common.by import By

class CommonLocators():
    HEADER = (By.ID, 'header')
    LOGO = (By.XPATH, '//*[@id="header"]/div/div/div[1]/a/img')
    CATEGORIES = (By.XPATH, '//*[@id="header"]/div/div/div[1]/div/div[2]')
    SEARCHBAR = (By.XPATH, '//*[@id="header"]/div/div/form/div/div')
    CART = (By.XPATH, '//*[@id="header"]/div/div/div[2]/div[1]/div[2]/button')
    ADD = (By.XPATH, '//*[@id="header"]/div/div/div[2]/div[1]/div[3]/button')
    USERDATA = (By.XPATH, '//*[@id="header"]/div/div/div[2]/div[2]/div/a')