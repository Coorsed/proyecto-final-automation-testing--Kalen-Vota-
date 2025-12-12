

import requests
import json
from pathlib import Path
from utils.logger import logger
import csv


def check_data(api_url, api_header, post_id):
    logger.info("Checking full data for verification")
    response = requests.get(f"{api_url}/{post_id}", headers=api_header)
    data = response.json()
    logger.info(data)


def json_reader(folder_name: str, file_name: str, search_key: str):
    data_path = Path(__file__).parent.parent / "data" / folder_name / file_name

    if not data_path.exists():
        raise FileNotFoundError(f"File '{file_name}' not found in 'data/{folder_name}' directory")
    
    with open(data_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if search_key not in data:
        raise KeyError(f"Search key '{search_key}' not found in {file_name}")
    
    return data[search_key]


def csv_reader(folder_name: str, file_name: str):
    inf=[]
    data_path = Path(__file__).parent.parent / "data" / folder_name / file_name
    
    if not data_path.exists():
        raise FileNotFoundError(f"File '{file_name}' not found in 'data/{folder_name}' directory")
    
    with open(data_path,newline='', encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
    
        for row in reader:
            expected = row["expected"].lower() == "true"

            inf.append((row['user'], row['password'],expected))
    return inf