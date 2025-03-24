from selenium.webdriver.common.by import By

class PasswordElement:
    locator = (By.NAME, "password")  # Using NAME locator

    @staticmethod
    def get_element(driver):
        return driver.find_element(*PasswordElement.locator)
