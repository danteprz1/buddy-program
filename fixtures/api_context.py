import pytest
from config.config import HEADERS
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def api_context():
    # Create a session-wide API context with authentication headers
    with sync_playwright() as p:
        request_context = p.request.new_context(extra_http_headers=HEADERS)
        yield request_context
        request_context.dispose()