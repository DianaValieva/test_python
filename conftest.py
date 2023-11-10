import pytest
from selene.support.shared import browser
from selene import be, have

@pytest.fixture(scope='session')
def set_browser_size():
    browser.driver.set_window_size(width=1000, height=1000)
    yield browser
    browser.quit()


@pytest.fixture()
def open_google(set_browser_size):
    browser.open('https://google.com')

