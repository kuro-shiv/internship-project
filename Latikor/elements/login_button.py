from selenium.webdriver.common.by import By

class LoginButton:
    locator = (By.CLASS_NAME, "btn_action")  # Using CLASS_NAME locator

    @staticmethod
    def get_element(driver):
        return driver.find_element(*LoginButton.locator)
