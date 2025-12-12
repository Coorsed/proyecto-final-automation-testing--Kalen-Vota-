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

        title = self.wait.until(EC.visibility_of_element_located(self._TITLE))
        return title.text

    def show_products(self):

        self.wait.until(EC.presence_of_all_elements_located(self._PRODUCTS))
        return self.driver.find_elements(*self._PRODUCTS)

    def add_first_product(self):

        buttons = self.wait.until(EC.presence_of_all_elements_located(self._ADD_BUTTONS))
        buttons[0].click()

    def cart_badge(self):

        try:
            badge = self.wait.until(EC.visibility_of_element_located(self._CART_BADGE))
            return int(badge.text)
        except:
            return 0

    def go_to_cart(self):

        cart = self.wait.until(EC.element_to_be_clickable(self._CART_LINK))
        cart.click()

    def logout(self):

        menu = self.wait.until(EC.element_to_be_clickable(self._MENU_BUTTON))
        menu.click()

        logout_btn = self.wait.until(EC.element_to_be_clickable(self._LOGOUT_LINK))
        logout_btn.click()