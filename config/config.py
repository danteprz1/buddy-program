# Description: Configuration file for the tests

#URLs
BASE_URL = "https://api.todoist.com/rest/v2"
PROJECT_URL = f"{BASE_URL}/projects"
TASK_URL = f"{BASE_URL}/tasks"

#Status codes
STATUS_OK = 200
STATUS_NO_CONTENT = 204
STATUS_BAD_REQUEST = 400
STATUS_NOT_FOUND = 404

#Data
INVALID_ID = 9999999999
NON_EXISTENT_ID = "test"
EMAIL = "dante.perez@wizeline.com"
MOCK_EMAIL = "test@test"

#TODO: Change this since it's sensible data
PASSWORD = "Lalala01!"