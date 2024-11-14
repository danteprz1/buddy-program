from fixtures.api_context import api_context
from fixtures.create_project import create_project
from config.config import *

def test_get_projects(api_context):
    response = api_context.get(f"{PROJECT_URL}")
    assert response.status == STATUS_OK
    assert isinstance(response.json(), list)

def test_create_project(api_context):
    project_data = {"name": "New Test Project"}
    response = api_context.post(f"{PROJECT_URL}", data=project_data)
    assert response.status == STATUS_OK
    assert response.json()["name"] == project_data["name"]

def test_get_project_with_id(api_context, create_project):
    project_id = create_project
    response = api_context.get(f"{PROJECT_URL}/{project_id}")
    assert response.status == STATUS_OK
    assert response.json()["id"] == project_id

def test_update_project(api_context, create_project):
    project_id = create_project
    updated_data = {"name": "Updated Project Name"}
    response = api_context.post(f"{PROJECT_URL}/{project_id}", data=updated_data)
    assert response.status == STATUS_OK

def test_delete_project(api_context, create_project):
    project_id = create_project
    response = api_context.delete(f"{PROJECT_URL}/{project_id}")
    assert response.status == STATUS_NO_CONTENT

def test_get_non_existent_project(api_context):
    invalid_project_id = INVALID_ID
    response = api_context.get(f"{PROJECT_URL}/{invalid_project_id}")
    assert response.status == STATUS_NOT_FOUND and response.text() == "Project not found"

def test_create_project_missing_name(api_context):
    response = api_context.post(f"{PROJECT_URL}", data={})
    assert response.status == STATUS_BAD_REQUEST

def test_update_non_existent_project(api_context):
    invalid_project_id = INVALID_ID
    response = api_context.post(f"{PROJECT_URL}/{invalid_project_id}", data={"name": "New name"})
    assert response.status == STATUS_NOT_FOUND

def test_delete_non_existent_project(api_context):
    invalid_project_id = NON_EXISTENT_ID
    response = api_context.delete(f"{PROJECT_URL}/{invalid_project_id}")
    assert response.status == STATUS_BAD_REQUEST