from selenium import webdriver 
from selenium.webdriver.common.by import By
import time


browser = webdriver.Chrome()
browser.get("https://www.selenium.dev/documentation/webdriver/")
browser.maximize_window()
title = browser.title
print(title)
assert "Selenium" in title


input("Press Enter to exit...")  # Keeps browser open
