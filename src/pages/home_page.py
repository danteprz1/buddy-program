from playwright.sync_api import Page

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.login_button = page.get_by_role("link", name="Log in")
        self.add_task_button = page.get_by_role("button", name="Add task")
        self.task_name_input = page.get_by_placeholder("Task name")
        self.submit_task_button = page.get_by_role("button", name="Add task")

    def navigate_to_login_page(self):
        self.login_button.click()

    def create_task(self, task_name: str):
        self.add_task_button.click()
        self.task_name_input.fill(task_name)
        self.submit_task_button.click()

    def is_task_present(self, task_name: str):
        return self.page.locator(f"text={task_name}").is_visible()