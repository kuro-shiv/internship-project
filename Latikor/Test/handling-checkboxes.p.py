import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
time.sleep(2)
browser.maximize_window()
time.sleep(3)



#use for scroll top to bottom

browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")
time.sleep(2)


#select single element


browser.find_element(By.XPATH,value="//label[normalize-space()='Sunday']").click()
time.sleep(2)

#for unchecking


browser.find_element(By.XPATH,value="//label[normalize-space()='Sunday']").click()
time.sleep(2)




#for all checkboxes


browser.execute_script("window.scrollTo(document.body.scrollHeight,0);")
time.sleep(2)
browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")
time.sleep(2)


checkboxes = browser.find_elements(By.XPATH,value="//input[@type='checkbox']")

for checkbox in checkboxes:
    checkbox.send_keys(Keys.SPACE)

checked_count =0

for checkbox in checkboxes:
    if checkbox.is_selected():
        checked_count +=1



expected_checked_count = 9


if checked_count == expected_checked_count:
    print('Checkbox count verified')
else:
    print('checkbox count mismatch')

time.sleep(5)