from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = Page
        self.emailField = page.get_by_label("Email")
        self.passwordField = page.get_by_label("Password")
        self.loginButton = page.get_by_role("button", name="Log in")
        self.invalidLoginMessage = page.get_by_text("Wrong email or password")

    def login(self, email, password):
        self.page.fill(self.emailField, email)
        self.page.fill(self.passwordField, password)
        self.page.click(self.loginButton)


