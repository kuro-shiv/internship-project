from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select


# 1st method of selection


driver = webdriver.Chrome()
time.sleep(1)
driver.get('https://the-internet.herokuapp.com/dropdown')
time.sleep(2)
driver.maximize_window()

dropdown = driver.find_element(By.XPATH,value='//select[@id="dropdown"]')
select = Select(dropdown)
time.sleep(2)


select.select_by_index(2)
time.sleep(2)
select.select_by_value("1")
time.sleep(2)
select.select_by_visible_text('Option 2')


time.sleep(3)

driver.refresh()
time.sleep(2)



#check case


dropdown = driver.find_element(By.XPATH,value='//select[@id="dropdown"]')

select = Select(dropdown)
option_count = len(select.options)

expected_count = 3  #count start from 0 so it's correct

if option_count == expected_count:
    print('test case passed. count is correct ')
else:
    print('This case fail. count is incorrect')




# 2nd method of selection



dropdown_element = driver.find_element(By.XPATH,value='//select[@id="dropdown"]')
target_value = "Option 2"
select2 = Select(dropdown_element)

for option in select2.options:
    if option.text == target_value:
        option.click()
        print(f"selected option is {target_value}")
        break

    else:
        print(f"option '{target_value}' not found")


time.sleep(5)