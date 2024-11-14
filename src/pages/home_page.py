from playwright.sync_api import Page

class HomePage:
    def __init__(self, page:Page):
        self.page = Page
        self.loginButton = page.get_by_role("link", name="Log in")

    def navigateToLoginPage(self):
        self.page.click(self.loginButton)