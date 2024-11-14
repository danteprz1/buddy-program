import pytest
from fixtures.api_context import api_context

BASE_URL = "https://api.todoist.com/rest/v2"

@pytest.fixture
def create_task(api_context):
    task_data = {"content": "New Task from Test"}
    response = api_context.post(f"{BASE_URL}/tasks", data=task_data)
    task_id = response.json()["id"]
    yield task_id
    api_context.delete(f"{BASE_URL}/projects/{task_id}")

