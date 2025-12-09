

import pytest
import json
import requests
from pathlib import Path
from utils.logger import logger
import pytest_check as check
from utils.helpers import json_reader


@pytest.fixture(scope="session")
def api_url():
    return json_reader("api.json","api_url")

@pytest.fixture(scope="session")
def api_header():
    return json_reader("api.json","api_header")

@pytest.fixture(scope="session")
def post_payload():
    return json_reader("payload.json","post")

@pytest.fixture(scope="session")
def put_payload():
    return json_reader("payload.json","put")

@pytest.fixture(scope="session")
def patch_payload():
    return json_reader("payload.json","patch")

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
