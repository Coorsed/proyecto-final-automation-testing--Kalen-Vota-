from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from utils.logger import logger
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.helpers import csv_reader

@pytest.mark.parametrize("user,password", csv_reader("saucedemo","login.csv",filter=True))
def test_inventory(login_in_driver, user, password):
    logger.info("Starting SCREENSHOT TEST")

    try:

        driver = login_in_driver
        logger.info("Performing login")
        LoginPage(driver).complete_login(user, password)
        logger.info(f"Login completed under user: {user}")

        inventory_page = InventoryPage(driver)
        logger.info("Verifying inventory page redirection")
        assert inventory_page.get_title() == "Products", "Inventory page title mismatch"
        logger.info("Redirected to inventory page successfully")
        
        assert len(inventory_page.show_products()) == 0, "The are products on inventory page"
        logger.info(f"Products are displayed: {len(inventory_page.show_products())} items found")

    except Exception as e:
        logger.error(f"Screenshot captured")
        raise

    logger.info("SCREENSHOT TEST completed")
    logger.info("-----------------------------------------------------------------------------------------------------")