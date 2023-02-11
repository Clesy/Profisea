from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

from helpers.links import DEMOBLAZE_URL
from pages.base.base_element import BaseElement
from pages.demoblaze.phone_page import PhonePage


class HomePageLocators:
    PHONE_LINK = (By.XPATH, "(//a[normalize-space()='Phones'])[1]")
    OPEN_PHONE_LINK = (By.XPATH, "(//a[@class='hrefch'])[1]")


class HomePage:
    def __init__(self, driver: Firefox):
        self.driver = driver
        self.element = BaseElement(self.driver)

        self.phone_category = self.driver.find_element(HomePageLocators.PHONE_LINK[0], HomePageLocators.PHONE_LINK[1])
        self.phone_link = self.driver.find_element(HomePageLocators.OPEN_PHONE_LINK[0],
                                                    HomePageLocators.OPEN_PHONE_LINK[1])

    def load(self):
        self.driver.get(DEMOBLAZE_URL)

    def go_to_phone(self):
        self.phone_category.click()
        self.phone_link.click()

        return PhonePage(self.driver)
