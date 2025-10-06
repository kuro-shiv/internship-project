from selenium import webdriver #import

browser = webdriver.Chrome() #driver
browser.get("https://www.selenium.dev/")
browser.maximize_window()
title = browser.title#printing title in terminal
print(title)
assert "Selenium" in title
print(title)