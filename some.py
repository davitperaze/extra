from driver import Driver
from selenium import webdriver as wb
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC

driver = wb.Chrome('chromedriver')
driver.maximize_window()
driver.get('https://extra.ge')
print(driver.title)


HEADER = (By.ID, 'header')
LOGO = (By.XPATH, '//*[@id="header"]/div/div/div[1]/a/img')
CATEGORIES = (By.XPATH, '//*[@id="header"]/div/div/div[1]/div/div[2]')
SEARCHBAR = (By.XPATH, '//*[@id="header"]/div/div/form/div/div')
CART = (By.XPATH, '//*[@id="header"]/div/div/div[2]/div[1]/div[2]/button')
ADD = (By.XPATH, '//*[@id="header"]/div/div/div[2]/div[1]/div[3]/button')
USERDATA = (By.XPATH, '//*[@id="header"]/div/div/div[2]/div[2]/div/a')


wt = Wait(driver, 10)
logo = wt.until(EC.visibility_of_element_located((LOGO)))

# logo = driver.find_element(*LOGO)


logost = logo.is_displayed()
print(logost)
cat = wt.until(EC.visibility_of_element_located((CATEGORIES)))

# cat = driver.find_element(*CATEGORIES)

cat.click()