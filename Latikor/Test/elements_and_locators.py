import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
time.sleep(1)
driver.get("https://www.google.co.in/")
time.sleep(2)
driver.maximize_window()
time.sleep(2)
title = driver.title
print(title)

search = driver.find_element(By.CSS_SELECTOR,value="#APjFqb")
time.sleep(1)
search.send_keys("hey",Keys.ENTER)
time.sleep(3)
driver.back()
browse = driver.find_element(By.CLASS_NAME,value='gb_X')
browse.send_keys(Keys.ENTER)
time.sleep(2)
driver.back()
time.sleep(2)
driver.refresh()
time.sleep(2)

driver.find_element(By.XPATH,value='//div[@class="FPdoLc lJ9FBc"]//input[@name="btnI"]').click()
time.sleep(3)

driver.back()
time.sleep(3)
