import pytest
from tests.ui.base_test import BaseTest

class TestPlaywrightSetup(BaseTest):
    @pytest.mark.skip
    def test_page_loads(self):
        # Navigate to login page
        self.page.goto("https://todoist.com/users/showlogin")

        # Verify that the login page loaded by checking the title
        assert "Todoist" in self.page.title(), "The page title does not contain 'Todoist'."