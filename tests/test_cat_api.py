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

def test_get_one_random_image(base_url):
    """Test retrieving one random image without API Key."""
    response = requests.get(f"{base_url}/images/search")
    assert response.status_code == 200, "Expected status code 200"
    json_data = response.json()
    assert len(json_data) == 1, "Expected one image to be returned"
    assert "url" in json_data[0], "Image URL should be present"
    print(f"Image URL: {json_data[0]['url']}")  # Log URL for the HTML report

def test_get_ten_random_images_with_api_key(base_url, headers):
    """Test retrieving 10 random images with API Key."""
    params = {"limit": 10}
    response = requests.get(f"{base_url}/images/search", headers=headers, params=params)
    assert response.status_code == 200, "Expected status code 200"
    json_data = response.json()
    assert len(json_data) == 10, "Expected 10 images to be returned"
    
    # Log each image URL to include it in the HTML report
    for image in json_data:
        print(f"Image URL: {image['url']}")

def test_get_image_by_id(base_url, headers):
    """Test retrieving a specific image by its ID."""
    image_id = "0XYvRd7oD" 
    response = requests.get(f"{base_url}/images/{image_id}", headers=headers)
    assert response.status_code == 200, "Expected status code 200"
    json_data = response.json()
    assert json_data["id"] == image_id, "Returned image ID should match requested ID"
    print(f"Specific Image URL: {json_data['url']}")  # Log URL for the HTML report

def test_get_images_by_category(base_url, headers):
    """Test retrieving images filtered by a specific category - hats."""
    category_id = 1  # Category ID for "hats"
    params = {"category_ids": category_id, "limit": 5}  # Request 5 images in the "hats" category
    response = requests.get(f"{base_url}/images/search", headers=headers, params=params)
    assert response.status_code == 200, "Expected status code 200"
    
    json_data = response.json()
    
    # Check if the API respected the limit
    if len(json_data) != 5:
        print(f"Warning: API returned {len(json_data)} images instead of the requested limit of 5.")
    
    # Assert that no more than 10 images were returned 
    assert len(json_data) <= 10, "Expected no more than 10 images to be returned"
    
    # Log each image URL to include it in the HTML report
    for image in json_data:
        print(f"Image URL: {image['url']}")

