from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests


driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/broken_images")
time.sleep(2)
driver.maximize_window()



# to find all img


images = driver.find_elements(By.TAG_NAME, value="img")

broken_images = []

for image in images :
    src = image.get_attribute("src")
    if src :
        response = requests.get(src)
        if response.status_code != 200:
            broken_images.append(src)
            print(f"Broken Image found")


if broken_images:
    print("List of broken images:")
    for broken_image in broken_images:
        print(broken_image)

else:
    print("No broken image")
