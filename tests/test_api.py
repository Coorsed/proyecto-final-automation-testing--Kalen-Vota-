

import requests
import pytest
from utils.logger import logger
from utils.helpers import check_data

def test_get(api_url, api_header):
    logger.info("Starting GET request test")
    response = requests.get(api_url, headers=api_header)

    logger.info(f"Response Status Code: {response.status_code}")
    assert response.status_code == 200, "Incorrect status code returned"

    data = response.json()
    assert len(data) > 0, "The list is empty"
    assert response.elapsed.total_seconds() < 1, "Slow API"
    logger.info("GET request test completed successfully")
    logger.info("-----------------------------------------------------------------------------------------------------")

def test_post(post_id):
    logger.info("Starting POST request test")
    logger.info(f"Post request test completed successfully and ID was created as {post_id}")
    logger.info("-----------------------------------------------------------------------------------------------------")


def test_put(api_url, api_header, put_payload, post_id):
    logger.info("Starting PUT request test")
    response = requests.put(f"{api_url}/{post_id}", headers=api_header, json=put_payload)

    assert response.status_code == 200, "Incorrect status code for PUT request"
    logger.info(f"Response Status Code: {response.status_code}")
    
    data = response.json()
    assert data["name"] == put_payload["name"], "Name in response does not match payload"
    assert data.get("job") is None, "Job field should not be present in PUT response"
    logger.info(data)
    check_data(api_url, api_header, post_id)
    assert response.elapsed.total_seconds() < 1, "Slow API"
    logger.info("PUT request test completed successfully")
    logger.info("-----------------------------------------------------------------------------------------------------")

def test_patch(api_url, api_header, patch_payload, post_id):
    logger.info("Starting PATCH request test")
    response = requests.patch(f"{api_url}/{post_id}", headers=api_header, json=patch_payload)

    assert response.status_code == 200, "Incorrect status code for PATCH request"
    logger.info(f"Response Status Code: {response.status_code}")
    
    data = response.json()
    assert data.get("name") is None, "Name field should not be present in PUT response"
    assert data["job"] == patch_payload["job"], "Job in response does not match payload"
    response = requests.get(api_url, headers=api_header)
    logger.info(data)
    check_data(api_url, api_header, post_id)
    assert response.elapsed.total_seconds() < 1, "Slow API"
    logger.info("PATCH request test completed successfully")
    logger.info("-----------------------------------------------------------------------------------------------------")

def test_delete(api_url, api_header, post_id):
    logger.info("Starting DELETE request test")
    response = requests.delete(f"{api_url}/{post_id}", headers=api_header)

    assert response.status_code == 204, "Incorrect status code for DELETE request"
    logger.info(f"Response Status Code: {response.status_code}")
    assert response.elapsed.total_seconds() < 1, "Slow API"
    check_data(api_url, api_header, post_id)
    logger.info("DELETE request test completed successfully")
    logger.info("-----------------------------------------------------------------------------------------------------")
