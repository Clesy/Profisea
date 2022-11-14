from selenium.webdriver import Firefox

from locators.locators import StorePage
from pages.base.base_page import BasePage
from pages.base.element import BasePageElement
from pages.demoblaze.cart_page import CartPage


class PhonePage(BasePage):
    def __init__(self, driver: Firefox):
        super().__init__(driver)

        self.element = BasePageElement(self.driver)
        self.page = StorePage()

    def go_to_cart(self):
        self.add_to_cart.click()
        self.cart_link.click()
        return CartPage(self.driver)

    @property
    def add_to_cart(self):
        return self.element.find_element(self.page.ADD_TO_CART_BTN[0], self.page.ADD_TO_CART_BTN[1])

    @property
    def cart_link(self):
        return self.element.find_element(self.page.CART_LINK[0], self.page.CART_LINK[1])
