

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    _TITLE = (By.CLASS_NAME, "title")
    _PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")
    _PRODUCT_PRICE = (By.CLASS_NAME, "inventory_item_price")
    _RETURN_INVENTORY = (By.ID, "continue-shopping")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_title(self):
        """get title of the page"""
        title = self.wait.until(EC.visibility_of_element_located(self._TITLE))
        return title.text

    def cart_product_name(self):
        """search the cart product name"""
        product_name = self.driver.find_elements(*self._PRODUCT_NAME)[0]
        return product_name.text

    def cart_product_price(self):
        """search the cart product price"""
        product_price = self.driver.find_elements(*self._PRODUCT_PRICE)[0]
        return product_price.text

    def return_inventory(self):
        """return to inventory page"""
        return_btn = self.wait.until(EC.element_to_be_clickable(self._RETURN_INVENTORY))
        return_btn.click()
