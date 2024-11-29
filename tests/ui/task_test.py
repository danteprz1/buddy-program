from playwright.sync_api import expect
from tests.ui.base_test import BaseTest

class TestTask(BaseTest):
    def test_create_new_task(self, user_valid_credentials):
        user, password = user_valid_credentials
        self.login_page.navigate_to_home_page(user, password)
        task_name = self.home_page.generate_random_task_name() + " Task"
        self.home_page.create_task(task_name)
        expect(self.home_page.is_task_present(task_name)).to_be_visible()
        self.mark_test_status("passed", "Successful creation of a task", self.page)
        self.cleanup()

    def test_create_multiple_tasks(self, user_valid_credentials):
        user, password = user_valid_credentials
        self.login_page.navigate_to_home_page(user, password)
        task_names = [f"Task {i}" for i in range(1, 11)]
        for task_name in task_names:
            self.home_page.create_task(task_name)
            expect(self.home_page.is_task_present(task_name)).to_be_visible()
        self.mark_test_status("passed", "Successful creation of multiple tasks", self.page)
        self.cleanup()

    def cleanup(self):
        self.home_page.task_cleanup()