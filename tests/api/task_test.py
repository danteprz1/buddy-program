from fixtures.api_context import api_context
from fixtures.create_task import create_task
from config.config import *

def test_get_tasks(api_context):
    """Test retrieving a list of tasks."""
    response = api_context.get(f"{TASK_URL}")
    assert response.status == STATUS_OK
    assert isinstance(response.json(), list)  # Expecting a list of tasks

def test_create_task(api_context):
    """Test creating a new task."""
    task_data = {"content": "New Task from Test"}
    response = api_context.post(f"{TASK_URL}", data=task_data)
    task = response.json()
    assert response.status == STATUS_OK and task["content"] == task_data["content"]

def test_get_task(api_context, create_task):
    """Test retrieving a specific task by ID."""
    task_id = create_task
    response = api_context.get(f"{TASK_URL}/{task_id}")
    assert response.status == STATUS_OK and response.json()["id"] == task_id

def test_update_task(api_context, create_task):
    """Test updating a task's content."""
    task_id = create_task
    updated_data = {"content": "Updated Task Content"}
    response = api_context.post(f"{TASK_URL}/{task_id}", data=updated_data)
    assert response.status == STATUS_OK  # Successful update response

    # Verify the update
    response = api_context.get(f"{TASK_URL}/{task_id}")
    assert response.json()["content"] == updated_data["content"]

def test_close_task(api_context, create_task):
    """Test marking a task as completed."""
    task_id = create_task
    response = api_context.post(f"{TASK_URL}/{task_id}/close")
    assert response.status == STATUS_NO_CONTENT

def test_reopen_task(api_context, create_task):
    """Test reopening a completed task."""
    task_id = create_task
    # First, close the task
    api_context.post(f"{TASK_URL}/{task_id}/close")

    # Now, reopen the task
    response = api_context.post(f"{TASK_URL}/{task_id}/reopen")
    assert response.status == STATUS_NO_CONTENT

def test_delete_task(api_context, create_task):
    """Test deleting a task."""
    task_id = create_task
    response = api_context.delete(f"{TASK_URL}/{task_id}")
    assert response.status == STATUS_NO_CONTENT

    # Verify deletion by trying to get the task
    response = api_context.get(f"{TASK_URL}/{task_id}")
    assert response.status == STATUS_NOT_FOUND  # Expecting a "not found" response

def test_get_non_existent_task(api_context):
    invalid_task_id = INVALID_ID
    response = api_context.get(f"{TASK_URL}/{invalid_task_id}")
    assert response.status == STATUS_NOT_FOUND
    assert response.text() == "Task not found"

def test_update_non_existent_task(api_context):
    invalid_task_id = INVALID_ID
    response = api_context.post(f"{TASK_URL}/{invalid_task_id}", data={"content": "New content"})
    assert response.status == STATUS_NOT_FOUND

def test_close_non_existent_task(api_context):
    invalid_task_id = INVALID_ID
    response = api_context.post(f"{TASK_URL}/{invalid_task_id}/close")
    assert response.status == STATUS_NOT_FOUND

def test_reopen_non_existent_task(api_context):
    invalid_task_id = INVALID_ID
    response = api_context.post(f"{TASK_URL}/{invalid_task_id}/reopen")
    assert response.status == STATUS_NOT_FOUND

def test_delete_non_existent_task(api_context):
    invalid_task_id = NON_EXISTENT_ID
    response = api_context.delete(f"{TASK_URL}/{invalid_task_id}")
    assert response.status == STATUS_BAD_REQUEST
