from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.email_field = page.get_by_label("Email")
        self.password_field = page.get_by_label("Password")
        self.login_button = page.get_by_role("button", name="Log in")
        self.invalid_login_message = page.get_by_text("Wrong email or password")

    def login(self, email: str, password: str):
        self.email_field.fill(email)
        self.password_field.fill(password)
        self.login_button.click()

    def is_login_successful(self):
        # Check if we successfully navigated to the home page or dashboard
        return self.page.url == "https://todoist.com/app"

    def is_login_unsuccessful(self):
        # Check if an error message is displayed
        return self.invalid_login_message.is_visible()


