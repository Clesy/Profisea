from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

from pages.base.base_element import BaseElement


class SuccessPurchasePopupLocators:
    SUCCESS_PURCHASE_TEXT = (By.XPATH, "// h2[normalize-space() = 'Thank you for your purchase!']")


class SuccessPurchasePopup:
    def __init__(self, driver: Firefox):
        self.driver = driver
        self.element = BaseElement(self.driver)

        self.success_purchase_text = self.element.find_element(SuccessPurchasePopupLocators.SUCCESS_PURCHASE_TEXT[0],
                                                               SuccessPurchasePopupLocators.SUCCESS_PURCHASE_TEXT[1])

    def get_success_purchase_text(self):
        return self.success_purchase_text.text
