import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://the-internet.herokuapp.com/nested_frames')
time.sleep(2)

# switching top frame


browser.switch_to.frame("frame-top")
time.sleep(2)

# switching middle frame


browser.switch_to.frame("frame-middle")
time.sleep(2)

content =browser.find_element(By.ID,value="content").text

print("Content in middle frame",content)
time.sleep(5)

# switch default content

browser.switch_to.default_content()
time.sleep(2)

# switch bottom content

browser.switch_to.frame("frame-bottom")
content_bottom = browser.find_element(By.TAG_NAME,value="body")
print("content in bottom frame",content_bottom)
time.sleep(5)




