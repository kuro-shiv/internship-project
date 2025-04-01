from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests

driver = webdriver.Chrome()
time.sleep(2)
driver.get('https://jqueryui.com/')
time.sleep(2)
driver.maximize_window()

# link anchor tags


all_links = driver.find_elements(By.TAG_NAME,value='a')
print(f'Total number of links on page : {len(all_links)}')
time.sleep(2)



# loop for a tag


for link in all_links:
    href = link.get_attribute('href')
    response = requests.get(href)

    if response.status_code >= 400: # for 404
        print(f"Broken link : {href}(status code : {response.status_code})")

driver.quit()