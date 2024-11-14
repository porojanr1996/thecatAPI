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