from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

from pages.base.base_element import BaseElement
from pages.demoblaze.place_order_popup import PlaceOrderPopup


class CardPageLocators:
    PLACE_ORDER_BTN = (By.XPATH, "//button[normalize-space()='Place Order']")


class CartPage:
    def __init__(self, driver: Firefox):
        self.driver = driver
        self.element = BaseElement(self.driver)

        self.place_order_btn = self.driver.find_element(CardPageLocators.PLACE_ORDER_BTN[0],
                                                        CardPageLocators.PLACE_ORDER_BTN[1])

    def press_place_order_btn(self):
        self.place_order_btn.click()
        return PlaceOrderPopup(self.driver)
