from selenium.webdriver import Firefox
from selenium.webdriver.common.alert import Alert

from locators.locators import BankManagerPageLocators
from pages.base.base_page import BasePage
from pages.base.element import BasePageElement


class BankManagerPage(BasePage):
    def __init__(self, driver: Firefox):
        super().__init__(driver)

        self.element = BasePageElement(self.driver)
        self.bank_manager = BankManagerPageLocators()

    def add_new_customer(self, first_name, last_name, post_code):
        self.add_customer_btn.click()
        self.first_name_input.send_keys(first_name)
        self.last_name_input.send_keys(last_name)
        self.post_code_input.send_keys(post_code)
        self.add_customer_submit_btn.click()

        alert = Alert(self.driver)
        alert.accept()

    def get_customer(self, value):
        self.customer_btn.click()
        self.customer_search.send_keys(value)
        return self.customer_info.text

    def click_process_btn(self, customer_name, currency_name="Pound"):
        self.open_account_btn.click()
        self.take_option(self.customer_list, customer_name)
        self.currency_list(currency_name).click()
        self.process_btn.click()

    def currency_list(self, currency_name):
        return self.element.find_element(self.bank_manager.CURRENCY_LIST[0],
                                         self.bank_manager.CURRENCY_LIST[1].format(currency_name))

    @staticmethod
    def take_option(list_, name):
        for c in list_:
            if c.text in name:
                c.click()

    @property
    def open_account_btn(self):
        return self.element.find_element(self.bank_manager.OPEN_ACCOUNT_BTN[0], self.bank_manager.OPEN_ACCOUNT_BTN[1])

    @property
    def process_btn(self):
        return self.element.find_element(self.bank_manager.PROCESS_BTN[0], self.bank_manager.PROCESS_BTN[1])

    @property
    def customer_list(self):
        select = self.element.find_element(self.bank_manager.CUSTOMER_LIST[0], self.bank_manager.CUSTOMER_LIST[1])
        return select.find_elements(self.bank_manager.LIST_OPTIONS[0],
                                    self.bank_manager.LIST_OPTIONS[1])

    @property
    def customer_btn(self):
        return self.element.find_element(self.bank_manager.CUSTOMER_BTN[0], self.bank_manager.CUSTOMER_BTN[1])

    @property
    def customer_info(self):
        return self.element.find_element(self.bank_manager.CUSTOMER_DATE[0], self.bank_manager.CUSTOMER_DATE[1])

    @property
    def customer_search(self):
        return self.element.find_element(self.bank_manager.SEARCH_CUSTOMER_INPUT[0],
                                         self.bank_manager.SEARCH_CUSTOMER_INPUT[1])

    @property
    def add_customer_btn(self):
        return self.element.find_element(self.bank_manager.ADD_CUSTOMER_BTN[0], self.bank_manager.ADD_CUSTOMER_BTN[1])

    @property
    def add_customer_submit_btn(self):
        return self.element.find_element(self.bank_manager.ADD_CUSTOMER_SUBMIT_BTN[0],
                                         self.bank_manager.ADD_CUSTOMER_SUBMIT_BTN[1])

    @property
    def first_name_input(self):
        return self.element.find_element(self.bank_manager.FIRST_NAME_INPUT[0], self.bank_manager.FIRST_NAME_INPUT[1])

    @property
    def last_name_input(self):
        return self.element.find_element(self.bank_manager.LAST_NAME_INPUT[0], self.bank_manager.LAST_NAME_INPUT[1])

    @property
    def post_code_input(self):
        return self.element.find_element(self.bank_manager.POST_CODE_INPUT[0], self.bank_manager.POST_CODE_INPUT[1])
