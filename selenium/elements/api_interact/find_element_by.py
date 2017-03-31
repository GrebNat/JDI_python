class By:
    @staticmethod
    def id():
        return NotImplemented

    @staticmethod
    def name():
        return NotImplemented

    @staticmethod
    def xpath(locator):
        return 'find_element_by_xpath', 'find_elements_by_xpath', locator

    @staticmethod
    def css(locator):
        return 'find_element_by_css_selector', 'find_elements_by_css_selector', locator

    @staticmethod
    def class_name(locator):
        return 'find_element_by_class_name', 'find_elements_by_class_name', locator