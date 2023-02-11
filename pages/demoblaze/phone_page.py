from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

from pages.base.base_element import BaseElement
from pages.demoblaze.cart_page import CartPage


class PhonePageLocators:
    CART_LINK = (By.XPATH, "//a[@id='cartur']")
    ADD_TO_CART_BTN = (By.XPATH, "//a[normalize-space()='Add to cart']")


class PhonePage:
    def __init__(self, driver: Firefox):
        self.driver = driver
        self.element = BaseElement(self.driver)

        self.card_link = self.element.find_element(PhonePageLocators.CART_LINK[0], PhonePageLocators.CART_LINK[1])
        self.add_to_cart = self.element.find_element(PhonePageLocators.ADD_TO_CART_BTN[0],
                                                     PhonePageLocators.ADD_TO_CART_BTN[1])

    def go_to_cart(self):
        self.add_to_cart.click()
        self.card_link.click()
        return CartPage(self.driver)
