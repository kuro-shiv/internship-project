
from selenium import webdriver 
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("https://selenium.dev/")
driver.maximize_window()
title = driver.title
print(title)
assert "Selenium" in title



driver.findElement(By.xpath(("#APjFqb")))


input("Press Enter to exit...")  # Keeps browser open