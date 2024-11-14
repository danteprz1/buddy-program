import pytest
from playwright.sync_api import Page

class BaseTest:
    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        """Playwright page instance for tests."""
        self.page = page