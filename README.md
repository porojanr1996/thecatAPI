# The Cat API Test Suite

This project is a test suite for The Cat API, created with Python's `requests` library and `pytest`. It aims to validate the functionality of The Cat API, particularly focusing on retrieving images, using an API key for authentication, and filtering images.

## Table of Contents
- [Setup](#setup)
- [Running the Tests](#running-the-tests)
- [Test Scenarios](#test-scenarios)
- [Project Structure](#project-structure)

---

## Setup

### 1. Clone the Repository
Clone the project repository to your local machine:
```bash
git clone <repository_url>
cd thecatAPI
```

### 2. Install Dependencies
Make sure to install the necessary dependencies listed in `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 3. Set Up the API Key
You will need an API key to access certain features of The Cat API. Follow these steps:
1. Obtain a free API key from [The Cat API](https://thecatapi.com/).
2. In  `.env` file and add your actual API key:
   ```plaintext
   CAT_API_KEY=your_api_key_here
   ```

---

## Running the Tests

Once the setup is complete, you can run the test suite and generate an HTML report to see detailed test results.

Run all tests with:
```bash
pytest --html=report.html
```

This will create an HTML report (`report.html`) in the project directory, which you can open in any browser to view the results.

---

## Test Scenarios

### 1. Retrieve One Random Image (No API Key)
   - **Description**: Tests retrieving a single random image without an API key.
   - **Expected Outcome**: The API should return a response with status `200`, containing one image with a valid URL.

### 2. Retrieve 10 Random Images (With API Key)
   - **Description**: Tests retrieving 10 random images using the API key.
   - **Expected Outcome**: The response status should be `200`, and the response should contain exactly 10 images, each with a valid URL.

### 3. Retrieve a Specific Image by ID
   - **Description**: Tests retrieving a specific image by its ID.
   - **Expected Outcome**: The response status should be `200`, and the image ID returned should match the requested ID.

### 4. Retrieve Images by Category (e.g., "Hats")
   - **Description**: Tests retrieving images filtered by a specific category "hats".
   - **Expected Outcome**: The response status should be `200`. Although 5 images are requested, the test handles cases where more images are returned due to API limitations and logs each image URL.

---

## Project Structure

Here’s a quick overview of the project’s structure:

```plaintext
thecatAPI/
├── tests/
│   ├── test_cat_api.py      # Contains test functions for each scenario
├── .env                     # Environment file to store API Key
├── README.md
├── requirements.txt         # List of dependencies
```

---