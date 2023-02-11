from selenium.webdriver import Firefox

from helpers.links import GLOBALS_QA_URL
from locators.locators import CustomerLoginPageLocators
from pages.base.base_page import BasePage
from pages.base.base_element import BaseElement
from pages.globalsqa.customer_page import CustomerPage


class CustomerLoginPage(BasePage):
    def __init__(self, driver: Firefox):
        super().__init__(driver)

        self.element = BaseElement(self.driver)
        self.customer_login_page = CustomerLoginPageLocators()

    def load(self):
        self.driver.get(GLOBALS_QA_URL)

    def take_user(self, user_name: str):
        select = self.users_list
        options_list = select.find_elements(self.customer_login_page.USERS_LIST_OPTIONS[0],
                                            self.customer_login_page.USERS_LIST_OPTIONS[1])

        for user in options_list:
            if user.text in user_name:
                user.click()

    def login(self):
        self.login_btn.click()
        return CustomerPage(self.driver)

    def is_displayed(self):
        return self.users_list.is_displayed()

    @property
    def login_btn(self):
        return self.element.find_element(self.customer_login_page.LOGIN_BTM[0], self.customer_login_page.LOGIN_BTM[1])

    @property
    def users_list(self):
        return self.element.find_element(self.customer_login_page.USERS_LIST[0],
                                         self.customer_login_page.USERS_LIST[1])
