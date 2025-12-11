

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    _TITLE = (By.CLASS_NAME, "title")
    _PRODUCTS = (By.CLASS_NAME, "inventory_item")
    _ADD_BUTTONS = (By.CSS_SELECTOR, "button[data-test*='add-to-cart']")
    _CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    _CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    _MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    _LOGOUT_LINK = (By.ID, "logout_sidebar_link")



    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_title(self):
        """get title of inventory page"""
        title = self.wait.until(EC.visibility_of_element_located(self._TITLE))
        return title.text

    def show_products(self):
        """show all the products availables"""
        return self.driver.find_elements(*self._PRODUCTS)

    def add_first_product(self):
        """add the first product available to the cart"""
        first_btn = self.driver.find_elements(*self._ADD_BUTTONS)[0]
        first_btn.click()

    def cart_badge(self):
        """get the amount of products in the cart"""
        try:
            badge = self.driver.find_element(*self._CART_BADGE)
            return int(badge.text)
        except:
            return 0

    def go_to_cart(self):
        """go to cart page"""
        self.driver.find_element(*self._CART_LINK).click()

    def logout(self):
        """page logout"""
        self.driver.find_element(*self._MENU_BUTTON).click()
        logout_link = self.wait.until(EC.element_to_be_clickable(self._LOGOUT_LINK))
        logout_link.click()