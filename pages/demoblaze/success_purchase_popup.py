from selenium.webdriver import Firefox

from locators.locators import StorePage
from pages.base.base_page import BasePage
from pages.base.element import BasePageElement


class SuccessPurchasePopup(BasePage):
    def __init__(self, driver: Firefox):
        super().__init__(driver)

        self.element = BasePageElement(self.driver)
        self.page = StorePage()

    def get_success_purchase_text(self):
        return self.success_purchase_text.text

    @property
    def success_purchase_text(self):
        return self.element.find_element(self.page.SUCCESS_PURCHASE_TEXT[0], self.page.SUCCESS_PURCHASE_TEXT[1])
