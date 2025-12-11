

import pytest
import requests
from utils.logger import logger
import pytest_check as check
from utils.helpers import json_reader
import pathlib
from datetime import datetime
from pytest_html import extras


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

    report_file = pathlib.Path(run_dir, "report.html")
    config.option.htmlpath = str(report_file)
    config.option.self_contained_html = True

    config.run_report_dir = run_dir


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    driver = (
        item.funcargs.get("driver")
        or item.funcargs.get("login_in_driver")
        or item.funcargs.get("browser")
    )

    if driver:
        report.page_url = driver.current_url

    if report.when == "call" and report.failed:

        run_dir = getattr(item.config, "run_report_dir", None)

        if driver and run_dir:
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            screenshot_name = f"{item.name}_{timestamp}.png"
            screenshot_path = pathlib.Path(run_dir, screenshot_name)

            driver.save_screenshot(str(screenshot_path))

            report.extra = getattr(report, "extra", [])

            html_thumbnail = f"""
            <a href="{screenshot_path.name}" target="_blank">
                <img src="{screenshot_path.name}" style="width:180px; border:1px solid #ff0000; border-radius:5px;">
            </a>
            """

            report.extra.append(extras.html(html_thumbnail))
