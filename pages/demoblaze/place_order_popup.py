from selenium.webdriver import Firefox

from locators.locators import StorePage
from pages.base.base_page import BasePage
from pages.base.element import BasePageElement
from pages.demoblaze.success_purchase_popup import SuccessPurchasePopup


class PlaceOrderPopup(BasePage):
    def __init__(self, driver: Firefox):
        super().__init__(driver)

        self.element = BasePageElement(self.driver)
        self.store_page = StorePage()

    def purchase(self, name, country, city, credit_cart, month, year):
        self.name_input.send_keys(name)
        self.country_input.send_keys(country)
        self.city_input.send_keys(city)
        self.credit_card_input.send_keys(credit_cart)
        self.month_input.send_keys(month)
        self.year_input.send_keys(year)
        self.purchase_btn.click()
        return SuccessPurchasePopup(self.driver)

    @property
    def name_input(self):
        return self.element.find_element(self.store_page.NAME_INPUT[0], self.store_page.NAME_INPUT[1])

    @property
    def country_input(self):
        return self.element.find_element(self.store_page.COUNTRY_INPUT[0], self.store_page.COUNTRY_INPUT[1])

    @property
    def city_input(self):
        return self.element.find_element(self.store_page.CITY_INPUT[0], self.store_page.CITY_INPUT[1])

    @property
    def credit_card_input(self):
        return self.element.find_element(self.store_page.CREDIT_CARD_INPUT[0], self.store_page.CREDIT_CARD_INPUT[1])

    @property
    def month_input(self):
        return self.element.find_element(self.store_page.MONTH_INPUT[0], self.store_page.MONTH_INPUT[1])

    @property
    def year_input(self):
        return self.element.find_element(self.store_page.YEAR_INPUT[0], self.store_page.YEAR_INPUT[1])

    @property
    def purchase_btn(self):
        return self.element.find_element(self.store_page.PURCHASE_BTN[0], self.store_page.PURCHASE_BTN[1])
