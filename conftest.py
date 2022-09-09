
from selene.support.shared import browser
import pytest


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.open('https://demoqa.com/automation-practice-form')
    browser.config.hold_browser_open = True
    yield
