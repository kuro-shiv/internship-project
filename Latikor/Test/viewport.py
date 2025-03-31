from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.get("https://aigen023.blogspot.com//") # Open OrangeHRM login page


#browser commands for viewport


time.sleep(5)
driver.fullscreen_window()
time.sleep(5)
driver.minimize_window()
time.sleep(5)
driver.maximize_window()
time.sleep(5)



# for certain size


driver.set_window_size(768,1024)
time.sleep(5)



#for multiple size


viewports = [(1024,768),(375,667),(414,896)]
try:
    for width,height in viewports :
        driver.set_window_size(width,height)
        time.sleep(4)

finally:
    driver.close()