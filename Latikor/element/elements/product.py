from selenium.webdriver.common.by import By

class ProductElement:
    locator = (By.XPATH, "//div[@class='inventory_item_name']")  # Using XPATH

    @staticmethod
    def get_element(driver):
        return driver.find_element(*ProductElement.locator)
