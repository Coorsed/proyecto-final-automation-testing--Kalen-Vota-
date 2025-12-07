import pytest
import json
import requests
from pathlib import Path
from utils.logger import logger

API_DATA = Path(__file__).parent / "data" / "api.json"

@pytest.fixture(scope="session")
def api_url():
    with open(API_DATA) as f:
        data = json.load(f) 
    return data["api_url"]

@pytest.fixture(scope="session")
def api_header():
    with open(API_DATA) as f:
        data = json.load(f)
    return data["api_header"]


PAYLOAD_DATA = Path(__file__).parent / "data" / "payload.json"

@pytest.fixture(scope="session")
def post_payload():
    with open(PAYLOAD_DATA) as f:
        data = json.load(f)
    return data["post"]

@pytest.fixture(scope="session")
def put_payload():
    with open(PAYLOAD_DATA) as f:
        data = json.load(f)
    return data["put"]

@pytest.fixture(scope="session")
def patch_payload():
    with open(PAYLOAD_DATA) as f:
        data = json.load(f)
    return data["patch"]

@pytest.fixture(scope="session")
def post_id(api_url, api_header, post_payload):
    response = requests.post(api_url, headers=api_header, json=post_payload)

    assert response.status_code == 201, "Incorrect status code for POST request"
    
    data = response.json()
    assert data["name"] == post_payload["name"], "Name in response does not match payload"
    assert data["job"] == post_payload["job"], "Job in response does not match payload"
    assert response.elapsed.total_seconds() < 1, "Slow API"

    post_id = data["id"]
    return post_id
