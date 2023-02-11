from selenium.webdriver import Firefox
from selenium.webdriver.common.alert import Alert

from locators.locators import BaseLocators
from pages.base.base_element import BaseElement


class BasePage(object):
    def __init__(self, driver: Firefox):
        self.driver = driver

        self.base_locators = BaseLocators()
        self.elements = BaseElement(driver)
        self.home_btn = self.elements.find_element(self.base_locators.HOME_BTN[0], self.base_locators.HOME_BTN[1])

    def click_home_btn(self):
        alert = Alert(self.driver)
        alert.accept()
        self.home_btn.click()
