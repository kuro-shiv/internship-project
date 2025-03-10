from selenium.webdriver.common.by import By

class UsernameElement:
    locator = (By.ID, "user-name")

    @staticmethod
    def get_element(driver):
        return driver.find_element(*UsernameElement.locator)
