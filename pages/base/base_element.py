from selenium.common import NoSuchElementException
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait


class BaseElement(object):
    def __init__(self, driver: Firefox):
        self.driver = driver
        self.locators = None

    def find_element(self, by=By.ID, value=None) -> WebElement:
        try:
            WebDriverWait(self.driver, 10).until(
                lambda driver_: self.driver.find_element(by, value)
            )
        except NoSuchElementException:
            print(f"Element by: {by} | value: {value} is not loaded")

        return self.driver.find_element(by, value)

    def find_elements(self, by=By.ID, value=None) -> list[WebElement]:
        try:
            WebDriverWait(self.driver, 10).until(
                lambda driver_: self.driver.find_elements(by, value)
            )
        except NoSuchElementException:
            print(f"Elements by: {by} | value: {value} is not loaded")

        return self.driver.find_elements(by, value)
