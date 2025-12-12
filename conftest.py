

import pytest
import requests
from utils.logger import logger
import pytest_check as check
from utils.helpers import json_reader
import pathlib
from datetime import datetime
from pytest_html import extras
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from pages.login_page import LoginPage

@pytest.fixture(scope="session")
def api_url():
    return json_reader("reqres","api.json","api_url")


@pytest.fixture(scope="session")
def api_header():
    return json_reader("reqres","api.json","api_header")


@pytest.fixture(scope="session")
def post_payload():
    return json_reader("reqres","payload.json","post")


@pytest.fixture(scope="session")
def put_payload():
    return json_reader("reqres","payload.json","put")


@pytest.fixture(scope="session")
def patch_payload():
    return json_reader("reqres","payload.json","patch")


@pytest.fixture(scope="session")
def post_id(api_url, api_header, post_payload):
    logger.info("Creating a new resource via POST request")
    response = requests.post(api_url, headers=api_header, json=post_payload)

    check.equal(response.status_code, 201, "Incorrect status code returned")
    
    data = response.json()
    check.equal(data["name"], post_payload["name"],"Name in response does not match payload")
    check.equal(data["job"], post_payload["job"],"Job in response does not match payload")
    check.is_true(response.elapsed.total_seconds() < 1, "Slow API")

    post_id = data["id"]
    return post_id


def pytest_configure(config):

    reports_dir = pathlib.Path("reports")
    reports_dir.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    run_dir = pathlib.Path(reports_dir, f"run_{timestamp}")
    run_dir.mkdir(exist_ok=True)

    screenshots_dir = pathlib.Path(run_dir, "screenshots")
    screenshots_dir.mkdir(exist_ok=True)

    report_file = pathlib.Path(run_dir, "report.html")
    config.option.htmlpath = str(report_file)
    config.option.self_contained_html = False

    config.screenshot_dir = screenshots_dir


def pytest_html_results_table_header(cells):

    cells.append('Screenshot')

def pytest_html_results_table_row(report, cells):

    screenshot_html = getattr(report, "screenshot_html", "-")
    cells.append(screenshot_html)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    driver = item.funcargs.get("driver")

    if report.when == "call" and report.failed and driver:
        screenshots_dir = item.config.screenshot_dir
        file_name = screenshots_dir / f"{item.name}.png"
        driver.save_screenshot(str(file_name))

        html_thumbnail = f"""
        <a href="screenshots/{file_name.name}" target="_blank">
            <img src="screenshots/{file_name.name}" style="width:120px; border:1px solid red; border-radius:5px;">
        </a>
        """
        report.screenshot_html = html_thumbnail


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--incognito")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--log-level=3")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_argument("--disable-gpu")
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    service = Service()
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 10)


@pytest.fixture
def login_in_driver(driver, user, password):
    LoginPage(driver).open()
    return driver


@pytest.fixture(scope="session")
def url_base():
    return json_reader("saucedemo","links.json","base_url")
