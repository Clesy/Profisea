from selenium.webdriver import Firefox

from locators.locators import HomePageLocators
from pages.globalsqa.bank_manager_page import BankManagerPage
from pages.base.base_page import BasePage
from pages.base.element import BasePageElement
from pages.globalsqa.customer_login_page import CustomerLoginPage


class HomePage(BasePage):
    def __init__(self, driver: Firefox):
        super().__init__(driver)

        self.element = BasePageElement(self.driver)
        self.home_locators = HomePageLocators()

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
