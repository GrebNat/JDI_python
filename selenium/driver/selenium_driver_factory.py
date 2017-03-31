from JDI import jdi_property
from JDI.selenium.driver.driver_types import DriverTypes
from selenium.webdriver.chrome.webdriver import WebDriver


class SeleniumDriverFactory:

    current_driver = None
  #  drivers = None

    # register driver
    def register_driver (self, driver):
        if DriverTypes.getDriverName(driver) == 'CHROME':
            global current_driver
            current_driver = self.register_chrome_driver()
            #drivers.append(current_driver)


    def register_chrome_driver(self):
        return WebDriver(jdi_property.selenium_chrome_driver_path)

    def register_local_driver(self, driver): raise NotImplemented()

    def set_run_type(self,runType): raise NotImplemented()

    #get driver
    def get_driver(self):
        if 'current_driver' not in dir(self):
            self.register_driver('chrome')
        global current_driver
        return current_driver

    #other
    def highlight(self, element):
        raise NotImplemented()

    def close(self):
        raise NotImplemented()


