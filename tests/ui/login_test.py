from playwright.sync_api import expect
from tests.ui.base_test import BaseTest

class TestLogin(BaseTest):
    def test_successful_login(self, user_valid_credentials):
        # Navigate to login page
        user, password = user_valid_credentials
        self.login_page.login(user, password)
        expect(self.home_page.settings_menu).to_be_visible()
        self.mark_test_status("passed", "Successful login", self.page)

    def test_unsuccessful_login_with_wrong_credentials(self, user_invalid_credentials):
        # Navigate to login page
        user, password = user_invalid_credentials
        self.login_page.login(user, password)
        expect(self.login_page.wrong_credentials_message).to_be_visible()
        self.mark_test_status("passed", "Unsuccessful login with invalid credentials", self.page)