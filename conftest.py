import pytest
from selene.support.shared import browser


@pytest.fixture(scope="session")
def open_browser():
    browser.driver.set_window_size(width=1920, height=1080)
    yield browser
    browser.quit()

@pytest.fixture()
def open_start_google(open_browser):
    browser.open('https://google.com')
