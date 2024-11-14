import pytest
from fixtures.api_context import api_context

BASE_URL = "https://api.todoist.com/rest/v2"

@pytest.fixture
def create_project(api_context):
    project_data = {"name": "Test Project"}
    response = api_context.post(f"{BASE_URL}/projects", data=project_data)
    project_id = response.json()["id"]
    yield project_id
    api_context.delete(f"{BASE_URL}/projects/{project_id}")
