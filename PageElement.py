from selenium.webdriver.support.ui import WebDriverWait  # using static class for returning element

TIME_OUT = 10


# this class including a static method of getting elements in a safe way with wait
# uses the Locators class formats for combining a proper method
class PageElement(object):
    @staticmethod
    def __set__(driver, value, by, param):
        element = WebDriverWait(driver, TIME_OUT).until(
            lambda driver: driver.find_element(by, param))
        element.clear()
        element.send_keys(value)

    @staticmethod
    def __get__(driver, by, param):
        element = WebDriverWait(driver, TIME_OUT).until(
            lambda driver: driver.find_element(by,param))
        return element