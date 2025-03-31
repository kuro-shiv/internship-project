from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")


# Login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()


print("✅ Login Successful!" if "inventory.html" in driver.current_url else "❌ Login Failed!")

input("Press Enter to exit...")  # Keeps browser open
