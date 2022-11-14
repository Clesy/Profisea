from selenium.webdriver import Firefox

from locators.locators import StorePage
from pages.base.base_page import BasePage
from pages.base.element import BasePageElement
from pages.demoblaze.place_order_popup import PlaceOrderPopup


class CartPage(BasePage):
    def __init__(self, driver: Firefox):
        super().__init__(driver)

        self.element = BasePageElement(self.driver)
        self.page = StorePage()

    def press_place_order_btn(self):
        self.place_order_btn.click()
        return PlaceOrderPopup(self.driver)

    @property
    def place_order_btn(self):
        return self.element.find_element(self.page.PLACE_ORDER_BTN[0], self.page.PLACE_ORDER_BTN[1])
