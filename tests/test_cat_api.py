import os
import requests
import pytest
from dotenv import load_dotenv

load_dotenv()

# API details
BASE_URL = "https://api.thecatapi.com/v1"
API_KEY = os.getenv("CAT_API_KEY")
HEADERS = {"x-api-key": API_KEY} if API_KEY else {}

@pytest.fixture
def base_url():
    return BASE_URL

@pytest.fixture
def headers():
    return HEADERS