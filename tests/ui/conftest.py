import pytest
from playwright.sync_api import sync_playwright
from config.config import BS_USERNAME, BS_ACCESS_KEY
import json
import urllib
import subprocess


@pytest.fixture(scope="session")
def playwright():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session")
def browser(playwright):

    desired_cap = {
            'os': 'osx',
            'os_version': 'big sur',
            'browser': 'playwright-chromium',
            'browser_version': 'latest',
            'browserstack.username': BS_USERNAME,
            'browserstack.accessKey': BS_ACCESS_KEY,
            'name': 'Test',
            'resolution': '1920x1080'
    }
    ws_endpoint = "wss://cdp.browserstack.com/playwright?caps=" + urllib.parse.quote(json.dumps(desired_cap))
    browser = playwright.chromium.connect(ws_endpoint)
    yield browser
    browser.close()

@pytest.fixture
def page(browser):
    context = browser.new_context()
    context.set_default_timeout(5000)
    page = context.new_page()
    yield page
    page.close()