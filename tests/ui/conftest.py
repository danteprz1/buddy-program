import json
import urllib
import pytest
from playwright.sync_api import sync_playwright
from config.config import BS_USERNAME, BS_ACCESS_KEY


@pytest.fixture(scope="session")
def playwright():
    with sync_playwright() as p:
        yield p

def pytest_addoption(parser):
    parser.addoption("--local", action="store", default="False", help="Run tests on local")

@pytest.fixture(scope="session")
def browser(request,playwright):
    local = request.config.option.local
    desired_cap = {
        'browserstack.username': BS_USERNAME,
        'browserstack.accessKey': BS_ACCESS_KEY,
        'os': 'Windows',
        'os_version': '10',
        'browser': 'playwright-chromium',
        'browser_version': 'latest',
        'project': 'Playwright UI',
        'name': 'Playwright UI Test on BrowserStack'
    }
    if local == "True":
        print("Running tests on local")
        browser = playwright.chromium.launch(headless=False)
    else:
        print("Running tests on BrowserStack")
        ws_endpoint = "wss://cdp.browserstack.com/playwright?caps=" + urllib.parse.quote(json.dumps(desired_cap))
        browser = playwright.chromium.connect(ws_endpoint)
    yield browser
    browser.close()


@pytest.fixture
def page(browser):
    context = browser.new_context()
    context.set_default_timeout(10000)
    page = context.new_page()
    yield page
    page.close()
