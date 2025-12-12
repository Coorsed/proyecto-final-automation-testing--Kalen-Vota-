from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.logger import logger
from utils.helpers import csv_reader
from utils.helpers import json_reader

@pytest.mark.parametrize("user,password", csv_reader("saucedemo","login.csv",filter=True))
def test_cart(login_in_driver, user, password, url_base):
    logger.info("Starting CART TEST")

    try:

        driver = login_in_driver
        logger.info("Performing login")
        LoginPage(driver).complete_login(user, password)
        logger.info(f"Login completed under user: {user}")

        inventory_page = InventoryPage(driver)
        logger.info("Verifying inventory page redirection")
        assert inventory_page.get_title() == "Products", "Inventory page title mismatch"
        logger.info("Redirected to inventory page successfully")

        inventory_page.add_first_product()
        logger.info("Added first product to cart")

        inventory_page.go_to_cart()
        logger.info("Navigated to cart page")

        cart_page = CartPage(driver)

        logger.info("Verifying cart page title")
        assert cart_page.get_title() == "Your Cart", "Cart page title mismatch"
        logger.info("Cart page title verified successfully")

        logger.info("Verifying product name & price in cart")
        assert cart_page.cart_product_name() == json_reader("saucedemo","products.json","item_1")["name"], "Product name in cart mismatch"
        assert cart_page.cart_product_price() == json_reader("saucedemo","products.json","item_1")["price"], "Product price in cart mismatch"
        logger.info("product name is : " + cart_page.cart_product_name())
        logger.info("product name list : " + str(json_reader("saucedemo","products.json","item_1")["name"]))
        logger.info("Product name & price in cart verified successfully")

        logger.info("Returning to inventory page from cart")
        cart_page.return_inventory()
        assert inventory_page.get_title() == "Products", "Failed to return to inventory page"
        logger.info("Returned to inventory page successfully")

        logger.info("Logging out")
        inventory_page.logout()
        assert url_base == driver.current_url, "Logout failed - URL mismatch"
        logger.info("Logged out successfully")

    except Exception as e:
        logger.error(f"Test failed for user: {user} with error: {e}")
        raise

    logger.info("CART TEST completed")
    logger.info("-----------------------------------------------------------------------------------------------------")
