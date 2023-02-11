import os

import pytest
from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture
def firefox_driver_setup():
    browser = webdriver.Firefox(executable_path=GeckoDriverManager().install(),
                                service_log_path=os.devnull,
                                options=firefox_options())
    browser.implicitly_wait(10)
    browser.fullscreen_window()
    yield browser
    browser.quit()


def firefox_options():
    options = FirefoxOptions()
    options.add_argument("--incognito")
    return options
