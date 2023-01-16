from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait


class BasePageElement(object):
    def __init__(self, driver: Firefox):
        self.driver = driver
        self.locators = None

    def find_element(self, by=By.ID, value=None) -> WebElement:
        WebDriverWait(self.driver, 10).until(
            lambda driver_: self.driver.find_element(by, value)
        )
        return self.driver.find_element(by, value)

    def find_elements(self, by=By.ID, value=None) -> list[WebElement]:
        WebDriverWait(self.driver, 10).until(
            lambda driver_: self.driver.find_elements(by, value)
        )
        return self.driver.find_elements(by, value)
