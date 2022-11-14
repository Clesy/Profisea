from selenium.webdriver import Firefox

from locators.locators import StorePage
from pages.base.base_page import BasePage
from pages.base.element import BasePageElement
from pages.demoblaze.phone_page import PhonePage


class HomePage(BasePage):
    def __init__(self, driver: Firefox):
        super().__init__(driver)

        self.element = BasePageElement(self.driver)
        self.page = StorePage()

    def go_to_phone(self):
        self.phone_category_link.click()
        self.open_phone_link.click()

        return PhonePage(self.driver)

    @property
    def phone_category_link(self):
        return self.element.find_element(self.page.PHONE_LINK[0], self.page.PHONE_LINK[1])

    @property
    def open_phone_link(self):
        return self.element.find_element(self.page.OPEN_PHONE_LINK[0], self.page.OPEN_PHONE_LINK[1])
