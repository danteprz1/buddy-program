import pytest
from playwright.sync_api import Page

from config.config import EMAIL, PASSWORD, MOCK_EMAIL
from src.pages.home_page import HomePage
from src.pages.login_page import LoginPage


class BaseTest:
    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        """Playwright page instance for tests."""
        self.page = page
        self.login_page = LoginPage(self.page)
        self.home_page = HomePage(self.page)
        self.page.goto("https://todoist.com/users/showlogin")

    @pytest.fixture
    def user_valid_credentials(self):
        return EMAIL, PASSWORD

    @pytest.fixture
    def user_invalid_credentials(self):
        return MOCK_EMAIL, PASSWORD