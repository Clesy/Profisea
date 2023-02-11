from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

from pages.base.base_element import BaseElement
from pages.demoblaze.success_purchase_popup import SuccessPurchasePopup


class PlaceOrderPopupLocators:
    NAME_INPUT = (By.XPATH, "//input[@id='name']")
    COUNTRY_INPUT = (By.XPATH, "//input[@id='country']")
    CITY_INPUT = (By.XPATH, "//input[@id='city']")
    CREDIT_CARD_INPUT = (By.XPATH, "//input[@id='card']")
    MONTH_INPUT = (By.XPATH, "//input[@id='month']")
    YEAR_INPUT = (By.XPATH, "//input[@id='year']")

    PURCHASE_BTN = (By.XPATH, "//button[normalize-space()='Purchase']")


class PlaceOrderPopup:
    def __init__(self, driver: Firefox):
        self.driver = driver
        self.element = BaseElement(self.driver)

        self.name_input = self.element.find_element(PlaceOrderPopupLocators.NAME_INPUT[0],
                                                    PlaceOrderPopupLocators.NAME_INPUT[1])
        self.country_input = self.element.find_element(PlaceOrderPopupLocators.COUNTRY_INPUT[0],
                                                       PlaceOrderPopupLocators.COUNTRY_INPUT[1])
        self.city_input = self.element.find_element(PlaceOrderPopupLocators.CITY_INPUT[0],
                                                    PlaceOrderPopupLocators.CITY_INPUT[1])
        self.credit_card_input = self.element.find_element(PlaceOrderPopupLocators.CREDIT_CARD_INPUT[0],
                                                           PlaceOrderPopupLocators.CREDIT_CARD_INPUT[1])
        self.month_input = self.element.find_element(PlaceOrderPopupLocators.MONTH_INPUT[0],
                                                     PlaceOrderPopupLocators.MONTH_INPUT[1])
        self.year_input = self.element.find_element(PlaceOrderPopupLocators.YEAR_INPUT[0],
                                                    PlaceOrderPopupLocators.YEAR_INPUT[1])
        self.purchase_btn = self.element.find_element(PlaceOrderPopupLocators.PURCHASE_BTN[0],
                                                      PlaceOrderPopupLocators.PURCHASE_BTN[1])

    def purchase(self, name, country, city, credit_cart, month, year):
        self.name_input.send_keys(name)
        self.country_input.send_keys(country)
        self.city_input.send_keys(city)
        self.credit_card_input.send_keys(credit_cart)
        self.month_input.send_keys(month)
        self.year_input.send_keys(year)
        self.purchase_btn.click()
        return SuccessPurchasePopup(self.driver)
