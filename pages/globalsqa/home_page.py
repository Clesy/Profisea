from selenium.webdriver import Firefox

from helpers.links import GLOBALS_QA_URL
from locators.locators import HomePageLocators
from pages.base.base_element import BaseElement
from pages.globalsqa.bank_manager_page import BankManagerPage
from pages.globalsqa.customer_login_page import CustomerLoginPage


class HomePage:
    def __init__(self, driver: Firefox):
        self.driver = driver
        self.element = BaseElement(self.driver)
        self.home_locators = HomePageLocators()

    def load(self):
        self.driver.get(GLOBALS_QA_URL)

    def customer_login(self):
        self.customer_login_btn.click()
        return CustomerLoginPage(self.driver)

    def bank_manager_login(self):
        self.bank_manager_btn.click()
        return BankManagerPage(self.driver)

    def is_displayed(self):
        return self.customer_login_btn.is_displayed() and self.bank_manager_btn.is_displayed()

    @property
    def customer_login_btn(self):
        return self.element.find_element(self.home_locators.CUSTOMER_LOGIN_BTN[0],
                                         self.home_locators.CUSTOMER_LOGIN_BTN[1])

    @property
    def bank_manager_btn(self):
        return self.element.find_element(self.home_locators.BANK_MANAGER_BTN[0], self.home_locators.BANK_MANAGER_BTN[1])
