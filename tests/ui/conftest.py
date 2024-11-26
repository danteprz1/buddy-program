import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def playwright():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session")
def browser(playwright):
    browser = playwright.chromium.launch(headless=True, slow_mo=2000)
    yield browser
    browser.close()

@pytest.fixture
def page(browser):
    context = browser.new_context()
    context.set_default_timeout(5000)
    page = context.new_page()
    yield page
    page.close()