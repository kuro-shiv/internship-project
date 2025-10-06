from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

time.sleep(5)
driver.maximize_window()
time.sleep(5)

driver.find_element(By.CSS_SELECTOR, value=".oxd-text.oxd-text--p.orangehrm-login-forgot-header").click()
time.sleep(5)
driver.back()
time.sleep(5)
driver.forward()
time.sleep(5)
driver.refresh()
time.sleep(5)

input("Press Enter to close...")

#driver.close()