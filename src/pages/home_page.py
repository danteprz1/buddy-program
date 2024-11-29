import string
import random
import pytest

from playwright.sync_api import Page

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.login_button = page.get_by_role("link", name="Log in")
        self.add_task_button = page.locator("button[class='plus_add_button']")
        self.cancel_task_button = page.get_by_label("Cancel")
        self.task_name_input = page.locator("p[data-placeholder='Task name']")
        self.submit_task_button = page.locator("button[type='submit']")
        self.settings_menu = page.locator('button[aria-label="Settings"]')
        self.created_task = "//div[contains(text(), 'String')]"
        self.task_radio_buttons = page.query_selector_all("button[aria-label='Mark as completed']")

    def navigate_to_login_page(self):
        self.login_button.click()

    def create_task(self, task_name: str):
        self.add_task_button.click()
        self.task_name_input.fill(task_name)
        self.submit_task_button.click()
        self.cancel_task_button.click()

    def is_task_present(self, task_name: str):
        return self.page.locator(self.created_task.replace("String", task_name))

    def task_cleanup(self):
        for task_radio_button in self.task_radio_buttons:
            task_radio_button.click()

    def generate_random_task_name(self):
        return ''.join(random.choices(string.ascii_letters, k=6))
