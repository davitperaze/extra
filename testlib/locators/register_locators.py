from selenium.webdriver.common.by import By

class RegisterLocators():
    BACK_BUTTON = (By.XPATH, '/html/body/app-root/app-sidebar/div[2]/app-sign-up-page/app-sign-user-info/div/div')
    FORM_TITLE = (By.XPATH, '/html/body/app-root/app-sidebar/div[2]/app-sign-up-page/app-sign-user-info/div/h3')
    
    NAME_INPUT = (By.XPATH, '/html/body/app-root/app-sidebar/div[2]/app-sign-up-page/app-sign-user-info/div/form/div[1]/div[1]/app-new-input/input')
    NAME_LABEL = (By.XPATH, '/html/body/app-root/app-sidebar/div[2]/app-sign-up-page/app-sign-user-info/div/form/div[1]/div[1]/app-new-input/label')

    LASTNAME_INPUT = (By.XPATH, '/html/body/app-root/app-sidebar/div[2]/app-sign-up-page/app-sign-user-info/div/form/div[1]/div[2]/app-new-input/input')
    LASTNAME_LABEL = (By.XPATH, '/html/body/app-root/app-sidebar/div[2]/app-sign-up-page/app-sign-user-info/div/form/div[1]/div[2]/app-new-input/label')

    EMAIL_INPUT = (By.XPATH, '/html/body/app-root/app-sidebar/div[2]/app-sign-up-page/app-sign-user-info/div/form/div[2]/app-new-input/input')
    EMAIL_LABEL = (By.XPATH, '/html/body/app-root/app-sidebar/div[2]/app-sign-up-page/app-sign-user-info/div/form/div[2]/app-new-input/label')

    DAY_INPUT = (By.XPATH, '/html/body/app-root/app-sidebar/div[2]/app-sign-up-page/app-sign-user-info/div/form/div[3]/div/app-new-date-picker/form/div/div/div[1]')
    DAY_LABEL = (By.XPATH, '/html/body/app-root/app-sidebar/div[2]/app-sign-up-page/app-sign-user-info/div/form/div[3]/div/app-new-date-picker/form/div/div/div[1]/app-new-select/ng-select/div/div/div[1]')
    DAY_LIST = (By.XPATH, '/html/body/app-root/app-sidebar/div[2]/app-sign-up-page/app-sign-user-info/div/form/div[3]/div/app-new-date-picker/form/div/div/div[1]/app-new-select/ng-select/ng-dropdown-panel/div[2]/div[2]')
    DAY_VAL = (By.XPATH, '/html/body/app-root/app-sidebar/div[2]/app-sign-up-page/app-sign-user-info/div/form/div[3]/div/app-new-date-picker/form/div/div/div[1]/app-new-select/ng-select/div/div/div[2]/span')

    MONTH_INPUT = (By.XPATH, '/html/body/app-root/app-sidebar/div[2]/app-sign-up-page/app-sign-user-info/div/form/div[3]/div/app-new-date-picker/form/div/div/div[2]')
    MONTH_LABEL = (By.XPATH, '/html/body/app-root/app-sidebar/div[2]/app-sign-up-page/app-sign-user-info/div/form/div[3]/div/app-new-date-picker/form/div/div/div[2]/app-new-select/ng-select/div/div/div[1]')
    MONTH_LIST = (By.XPATH, '/html/body/app-root/app-sidebar/div[2]/app-sign-up-page/app-sign-user-info/div/form/div[3]/div/app-new-date-picker/form/div/div/div[2]/app-new-select/ng-select/ng-dropdown-panel/div[2]/div[2]')
    MONTH_VAL = (By.XPATH, '/html/body/app-root/app-sidebar/div[2]/app-sign-up-page/app-sign-user-info/div/form/div[3]/div/app-new-date-picker/form/div/div/div[2]/app-new-select/ng-select/div/div/div[2]/span')

    YEAR_INPUT = (By.XPATH, '/html/body/app-root/app-sidebar/div[2]/app-sign-up-page/app-sign-user-info/div/form/div[3]/div/app-new-date-picker/form/div/div/div[3]')
    YEAR_LABEL = (By.XPATH, '/html/body/app-root/app-sidebar/div[2]/app-sign-up-page/app-sign-user-info/div/form/div[3]/div/app-new-date-picker/form/div/div/div[3]/app-new-select/ng-select/div/div/div[1]')
    YEAR_LIST = (By.XPATH, '/html/body/app-root/app-sidebar/div[2]/app-sign-up-page/app-sign-user-info/div/form/div[3]/div/app-new-date-picker/form/div/div/div[3]/app-new-select/ng-select/ng-dropdown-panel/div[2]/div[2]')
    YEAR_VAL = (By.XPATH, '/html/body/app-root/app-sidebar/div[2]/app-sign-up-page/app-sign-user-info/div/form/div[3]/div/app-new-date-picker/form/div/div/div[3]/app-new-select/ng-select/div/div/div[2]/span')

    REGISTER_BUTTON = (By.XPATH, '/html/body/app-root/app-sidebar/div[2]/app-sign-up-page/app-sign-user-info/div/form/div[4]/button')