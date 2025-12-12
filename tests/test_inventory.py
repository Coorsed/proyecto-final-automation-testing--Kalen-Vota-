from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from utils.logger import logger
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.helpers import csv_reader

@pytest.mark.parametrize("user,password", csv_reader("saucedemo","login.csv",filter=True))
def test_inventory(login_in_driver, user, password):
    logger.info("Starting inventory test")

    try:

        driver = login_in_driver
        logger.info("Performing login")
        LoginPage(driver).complete_login(user, password)
        logger.info(f"Login completed under user: {user}")

        inventory_page = InventoryPage(driver)
        logger.info("Verifying inventory page redirection")
        assert inventory_page.get_title() == "Products", "Inventory page title mismatch"
        logger.info("Redirected to inventory page successfully")
        
        assert len(inventory_page.show_products()) > 0, "No products found on inventory page"
        logger.info(f"Products are displayed: {len(inventory_page.show_products())} items found")

        assert inventory_page.cart_badge() == 0, "Cart badge should be 0 initially"
        logger.info("Initial cart badge is 0 as expected")

        inventory_page.add_first_product()
        logger.info("Added first product to cart")

        assert inventory_page.cart_badge() == 1, "Cart badge should be 1 after adding a product"
        logger.info("Cart badge updated to 1 after adding a product")

    except Exception as e:
        print(f"Test failed for user: {user} with error: {e}")
        logger.error(f"Test failed for user: {user} with error: {e}")
        raise

    logger.info("Inventory test completed")
    logger.info("-----------------------------------------------------------------------------------------------------")