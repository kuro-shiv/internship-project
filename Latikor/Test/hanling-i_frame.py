from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/iframe")
time.sleep(2)

extra = driver.find_element(By.XPATH, value='//*[name()="path" and contains(@d,"M17.3 8.2L")]')
extra.click()
time.sleep(2)

iframe = driver.find_element(By.ID,value="mce_0_ifr")
driver.switch_to.frame(iframe)
time.sleep(2)

Text_Editor = driver.find_element(By.ID,value="tinymce")
Text_Editor.clear()
time.sleep(2)

Text_Editor.send_keys("This is example of how to send keys")
time.sleep(5)

driver.switch_to.default_content()
selenium_link = driver.find_element(By.ID,value='//a[normalize-space()="Elemental Selenium"]')
selenium_link.click()
time.sleep(5)