import time
from selenium.webdriver.common.by import By
from selenium import webdriver

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://cosmocode.io/automation-practice-webtable/")
time.sleep(2)


# mid or any loc stop in scrolling

browser.execute_script("window.scrollTo(0,700)")
time.sleep(3)
table = browser.find_element(By.ID, value="countries")
rows = table.find_elements(By.TAG_NAME,value = "tr")
row_count = len(rows)
print(row_count)
target_value = "Australia"
found = False

for row in rows:
    cells = row.find_elements(By.TAG_NAME,value="td")
    for cell in cells:
        if target_value in cell.text:
            print(f"found value {target_value}")
            found = True
            break
    if found:
        break
if not found:
    print(f"not found value {target_value}")