import pytest
from playwright.sync_api import sync_playwright
from urllib import parse

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
        "browserstack.networkLogs": True,
        "browserstack.local": True,
        "browserstack.console": "errors",
        "browserstack.username": {BS_USERNAME},
        "browserstack.accessKey": {BS_ACCESS_KEY}
    }
    caps = parse.urlencode(capabilities)
    ws_endpoint = f"wss://cdp.browserstack.com/playwright?caps={caps}"
    browser = playwright.chromium.connect_over_cdp(ws_endpoint)
    yield browser
    browser.close()

@pytest.fixture
def page(browser):
    context = browser.new_context()
    context.set_default_timeout(5000)
    page = context.new_page()
    yield page
    page.close()