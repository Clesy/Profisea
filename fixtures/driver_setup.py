import pytest
from selenium.webdriver import FirefoxOptions, Firefox


@pytest.fixture
def firefox_driver_setup():
    browser = Firefox(executable_path="../geckodriver", options=firefox_options())
    browser.fullscreen_window()
    yield browser
    browser.quit()


def firefox_options():
    options = FirefoxOptions()
    options.add_argument("--incognito")
    return options
