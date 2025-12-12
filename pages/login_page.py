from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import json_reader
import time

class LoginPage:
    URL = json_reader("saucedemo","links.json","base_url")
    _USER_INPUT = (By.ID, "user-name")
    _PASSWORD_INPUT = (By.ID, "password")
    _LOGIN_BUTTON = (By.ID, "login-button")
    _ERROR_MESSAGE = (By.CSS_SELECTOR, ".error-message-container h3")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)
        return self

    def fill_user(self, user: str):
        field = self.wait.until(EC.visibility_of_element_located(self._USER_INPUT))
        field.clear()
        field.send_keys(user)
        return self

    def fill_password(self, password: str):
        field = self.wait.until(
            EC.visibility_of_element_located(self._PASSWORD_INPUT)
        )
        field.clear()
        field.send_keys(password)
        return self

    def click_login(self):
        self.wait.until(
            EC.element_to_be_clickable(self._LOGIN_BUTTON)
        ).click()

    def complete_login(self, user, password):
        self.fill_user(user)
        self.fill_password(password)
        self.click_login()
        return self

    def error_content(self) -> str:
        error = self.wait.until(
            EC.visibility_of_element_located(self._ERROR_MESSAGE)
        )
        return error.text