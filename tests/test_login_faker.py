from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from utils.logger import logger
from pages.login_page import LoginPage
from faker import Faker

@pytest.mark.parametrize("user,password,expected",[(Faker().user_name(), Faker().password(length=8,special_chars=True,upper_case=True,lower_case=True,digits=True), False)])
def test_login(login_in_driver, user, password, expected):

    logger.info(f"Starting FAKER TEST for user={user}, password={password}, expected={expected}")
    driver = login_in_driver

    LoginPage(driver).complete_login(user,password)

    if expected == True:
        logger.info("Verifying successful login by checking URL")

        try:
            assert "/inventory.html" in driver.current_url, "Login failed - URL mismatch"
            logger.info(f"Login successful for user: {user}")
            
        except AssertionError as e:
            logger.info(f"Login test failed for user: {user} - {str(e)}")

    elif expected == False:
        error_message = LoginPage(driver).error_content()
        assert "Epic sadface" in error_message, "Expected an error message but none was found"
        logger.info(f"Login failed as expected for user: {user} with error: {error_message} successfully verified")

    logger.info("FAKER TEST completed")
    logger.info("-----------------------------------------------------------------------------------------------------")