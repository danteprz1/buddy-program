import os
from playwright.sync_api import sync_playwright
import pytest

#API_TOKEN = os.getenv("TODOIST_API_TOKEN")
API_TOKEN = "42e100a23d1dfb7f5cc70717fa5fc92ccc176476"
BASE_URL = "https://api.todoist.com/rest/v2"
HEADERS = {"Authorization": f"Bearer {API_TOKEN}"}

@pytest.fixture(scope="function")
def api_context():
    """Create a session-wide API context with authentication headers."""
    with sync_playwright() as p:
        request_context = p.request.new_context(extra_http_headers=HEADERS)
        yield request_context
        request_context.dispose()