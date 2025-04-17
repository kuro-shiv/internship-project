from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://the-internet.herokuapp.com/javascript_alerts')
time.sleep(2)

#JS Alert

alert_button = browser.find_element(By.XPATH,value='//button[normalize-space()="Click for JS Alert"]')
alert_button.click()
time.sleep(2)
alert = browser.switch_to.alert
alert_text = alert.text
print(alert_text)
time.sleep(2)
alert.accept()
time.sleep(3)

#JS Confirm

confirm = browser.find_element(By.XPATH,value='//button[normalize-space()="Click for JS Confirm"]')
confirm.click()
time.sleep(2)
alert_2 = browser.switch_to.alert
confirm_js = alert_2.text
print(confirm_js)
time.sleep(2)
alert.dismiss()
time.sleep(3)
#JS prompt

prompt = browser.find_element(By.XPATH,value='//button[normalize-space()="Click for JS Prompt"]')
prompt.click()
time.sleep(2)
alert.send_keys("This is test case")
time.sleep(2)
alert.accept()
time.sleep(3)