from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize WebDriver
driver = webdriver.Chrome()
driver.get("https://www.google.com")

# Locate search box and perform search
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium automation with Python")
search_box.send_keys(Keys.RETURN)

# Wait for results
time.sleep(3)

# Extract and print titles of results
results = driver.find_elements(By.CSS_SELECTOR, "h3")
for idx, result in enumerate(results):
    print(f"{idx + 1}. {result.text}")

# Close the browser
driver.quit()
