import pytest
from playwright.sync_api import sync_playwright
from config.config import BS_USERNAME, BS_ACCESS_KEY


@pytest.fixture(scope="session")
def playwright():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session")
def browser(playwright):
    capabilities = {
        "browser": "playwright-chromium",
        "browser_version": "latest",
        "os": "osx",
        "os_version": "catalina",
    }
    ws_endpoint = f"wss://cdp.browserstack.com/playwright?auth={BS_USERNAME}:{BS_ACCESS_KEY}"
    browser = playwright.chromium.connect(ws_endpoint, **capabilities)
    yield browser
    browser.close()

@pytest.fixture
def page(browser):
    context = browser.new_context()
    context.set_default_timeout(5000)
    page = context.new_page()
    yield page
    page.close()