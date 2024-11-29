# Description: Configuration file for the tests
import os

#Data
INVALID_ID = 9999999999
NON_EXISTENT_ID = "test"
EMAIL = os.getenv("USER_EMAIL")
MOCK_EMAIL = "test@test"
PASSWORD = os.getenv("USER_PASSWORD")
API_TOKEN = os.getenv("API_TOKEN")
BS_USERNAME = os.getenv("BROWSERSTACK_USERNAME")
BS_ACCESS_KEY = os.getenv("BROWSERSTACK_ACCESS_KEY")

#URLs
BASE_URL = "https://api.todoist.com/rest/v2"
PROJECT_URL = f"{BASE_URL}/projects"
TASK_URL = f"{BASE_URL}/tasks"
HEADERS = {"Authorization": f"Bearer {API_TOKEN}"}

#Status codes
STATUS_OK = 200
STATUS_NO_CONTENT = 204
STATUS_BAD_REQUEST = 400
STATUS_NOT_FOUND = 404