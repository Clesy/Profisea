import time
from datetime import datetime

from selenium.webdriver import Firefox

from helpers.links import GLOBALS_QA_URL
from locators.locators import CustomerPageLocators, BaseLocators
from pages.base.base_element import BaseElement


class CustomerPage:
    def __init__(self, driver: Firefox):
        self.driver = driver
        self.element = BaseElement(self.driver)
        self.customer_page = CustomerPageLocators()

        self.date = driver.find_element(self.customer_page.TRANSACTION_DATE[0], self.customer_page.TRANSACTION_DATE[1])

    def load(self):
        self.driver.get(GLOBALS_QA_URL)

    def deposit(self, amount):
        self.deposit_btn.click()
        time.sleep(2)
        self.deposit_input.send_keys(amount)
        self.deposit_input_btn.click()

    def notification(self):
        return self.transaction_notification

    def transactions_date(self):
        self.transaction_btn.click()
        date = datetime.strptime(self.date.text, "%b %d, %Y %H:%M:%S PM")
        return date

    def get_transaction_amount(self):
        self.transaction_btn.click()
        return self.transaction_amount.text

    def get_transactions_amount(self):
        self.transaction_btn.click()
        return self.transactions_amount

    def withdraw_transaction(self, amount):
        self.withdraw_btn.click()
        time.sleep(2)
        self.withdraw_input.send_keys(amount)
        self.withdraw_input_btn.click()

    def logout(self):
        base_locators = BaseLocators()
        self.element.find_element(base_locators.LOGOUT_BTN[0], base_locators.LOGOUT_BTN[1]).click()

    def get_welcome_text(self):
        return self.welcome_text.text

    @property
    def welcome_text(self):
        return self.element.find_element(self.customer_page.WELCOME_USER_TEXT[0],
                                         self.customer_page.WELCOME_USER_TEXT[1])

    @property
    def transaction_notification(self):
        return self.element.find_element(self.customer_page.TRANSACTIONS_NOTIFICATION[0],
                                         self.customer_page.TRANSACTIONS_NOTIFICATION[1]).text

    @property
    def deposit_btn(self):
        return self.element.find_element(self.customer_page.DEPOSIT_BTN[0], self.customer_page.DEPOSIT_BTN[1])

    @property
    def deposit_input(self):
        return self.element.find_element(self.customer_page.DEPOSIT_INPUT[0], self.customer_page.DEPOSIT_INPUT[1])

    @property
    def deposit_input_btn(self):
        return self.element.find_element(self.customer_page.DEPOSIT_INPUT_BTN[0],
                                         self.customer_page.DEPOSIT_INPUT_BTN[1])

    @property
    def transactions_amount(self):
        return self.element.find_elements(self.customer_page.TRANSACTION_AMOUNT[0],
                                          self.customer_page.TRANSACTION_AMOUNT[1])

    @property
    def transaction_amount(self):
        return self.element.find_element(self.customer_page.TRANSACTION_AMOUNT[0],
                                         self.customer_page.TRANSACTION_AMOUNT[1])

    @property
    def transaction_btn(self):
        return self.element.find_element(self.customer_page.TRANSACTION_BTN[0], self.customer_page.TRANSACTION_BTN[1])

    @property
    def withdraw_btn(self):
        return self.element.find_element(self.customer_page.WITHDRAW_BTN[0], self.customer_page.WITHDRAW_BTN[1])

    @property
    def withdraw_input(self):
        return self.element.find_element(self.customer_page.WITHDRAW_INPUT[0], self.customer_page.WITHDRAW_INPUT[1])

    @property
    def withdraw_input_btn(self):
        return self.element.find_element(self.customer_page.WITHDRAW_INPUT_BTN[0],
                                         self.customer_page.WITHDRAW_INPUT_BTN[1])
