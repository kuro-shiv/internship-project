from selenium import webdriver
from selenium.webdriver.common.by import By
import time




driver = webdriver.Chrome()
driver.get("https://www.amazon.com/")





driver.find_element(By.LINK_TEXT, "Sign in").click()




time.sleep(2) 




driver.find_element(By.ID, "ap_email").send_keys("email@example.com")
driver.find_element(By.NAME, "continue").click()





time.sleep(2)  




driver.quit()
print("Test completed!")
