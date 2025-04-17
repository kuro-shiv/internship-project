from selenium import webdriver
import time
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://www.globalsqa.com/demo-site/datepicker/')
time.sleep(2)

browser.find_element(By.XPATH,value='//div[@class="single_tab_div resp-tab-content resp-tab-content-active"]//a[@class="close_img"]')
frame_lo = browser.find_element(By.XPATH,value="//iframe[@class='demo-frame lazyloaded']")
browser.switch_to.frame()

key_1 = browser.find_element(By.XPATH,value='//li[@id="Simple Date Picker"]')
key_1.click()
time.sleep(2)
browser.find_element(By.XPATH,value='//input[@id="datepicker"]').click()
time.sleep(6)
