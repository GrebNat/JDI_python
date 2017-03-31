import logging

from JDI.selenium.driver.selenium_driver_factory import SeleniumDriverFactory
from JDI.selenium.elements.api_interact.find_element_by import By
from JDI.util.decorators import constant


class GetElementModule(object):
    @constant
    def FAILED_TO_FIND_ELEMENT_MESSAGE(self): return "Can't find Element '%s' during "

    @constant
    def FIND_TO_MUCH_ELEMENTS_MESSAGE(self): return "Find %s elements instead of one for Element '%s' during "

    byLocators = None
    locator = None
    web_element = None
    element = None
    frameLocator = None
    web_elements = []
    find_element_function = None
    find_elements_function = None

    def __init__(self, by):
        self.find_element_function, self.find_elements_function, self.locator = by

    def get_element(self):
        el = None
        if self.web_element is not None:
            el = self.web_element
        else:
            el = self._get_element_action()
        return el

    def _get_element_action(self):
        element_list = self._get_elements_action()
        if len(element_list) is 0:
            raise Exception(GetElementModule.FAILED_TO_FIND_ELEMENT_MESSAGE % self.locator)
        elif len(element_list) is 1:
            return element_list[0]
        else:
            raise Exception (GetElementModule.FIND_TO_MUCH_ELEMENTS_MESSAGE % len(element_list), self.locator)

    def _get_elements_action(self):
        if len(self.web_elements) is not 0:
            return self.web_elements
        result = self._search_elements()
        if result is None or len(result) is 0:
            logging.fatal("Can't get Web Elements")
        else:
            self.web_elements = result
        return result

    def _search_elements(self):
        return self._get_driver().__getattribute__(self.find_elements_function)(self.locator)

    def _get_driver(self):
        return SeleniumDriverFactory().get_driver()


SeleniumDriverFactory().register_driver('chrome')
SeleniumDriverFactory().get_driver().maximize_window()
SeleniumDriverFactory().get_driver().get("https://jdi-framework.github.io/tests/")

gem = GetElementModule(By.css("header .search"))
el = gem.get_element()
el.click()
el.click()

SeleniumDriverFactory().get_driver().quit()



