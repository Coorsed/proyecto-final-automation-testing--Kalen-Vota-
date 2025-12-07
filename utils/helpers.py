import requests
from utils.logger import logger

def check_data(api_url, api_header, post_id):
    logger.info("Checking full data for verification")
    response = requests.get(f"{api_url}/{post_id}", headers=api_header)
    data = response.json()
    logger.info(data)