from selenium import webdriver
from elements.username import UsernameElement
from elements.password import PasswordElement
from elements.login_button import LoginButton
from elements.product import ProductElement
import time

# Setup WebDriver
driver = webdriver.Chrome()

try:
    # Open SauceDemo
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    # Interact with username field
    username = UsernameElement.get_element(driver)
    username.send_keys("standard_user")

    # Interact with password field
    password = PasswordElement.get_element(driver)
    password.send_keys("secret_sauce")

    # Click login button
    login_button = LoginButton.get_element(driver)
    login_button.click()

    time.sleep(2)  # Wait for page load

    # Interact with product
    product = ProductElement.get_element(driver)
    print("First Product Name:", product.text)

  # Close browser
finally:
    print("code run")