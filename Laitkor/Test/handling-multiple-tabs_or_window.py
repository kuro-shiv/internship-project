from selenium import webdriver
import time
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://www.selenium.dev/")
time.sleep(2)

browser.switch_to.new_window()
browser.get("https://playwright.dev/")
time.sleep(10)




# number of tabs are currently open


number_of_tabs = len(browser.window_handles)
print(number_of_tabs)



# Value of tabs currently open


tabs_value = browser.window_handles
print(tabs_value)




# Value of tab which is  currently open


current_tab = browser.current_window_handle
print(current_tab)




#switching window


browser.find_element(By.XPATH, value='//a[normalize-space()="Get started"]').click()
first_tab = browser.window_handles[0]
time.sleep(2)


if current_tab != first_tab:
    browser.switch_to.window(first_tab)
browser.find_element(By.XPATH, value='//span[normalize-space()="Downloads"]').click()
time.sleep(3)