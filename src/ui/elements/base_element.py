from selenium.webdriver.common.by import By


class BaseElement(object):

    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator

    def is_enabled(self):
        """"""
        return self.web_element.is_enabled()

    def is_displayed(self):
        """Wrapper for Web Element is_displayed Method"""
        return len(self._find_all_by_locator()) > 0

    def is_selected(self):
        """"""
        return self._find_by_locator().is_selected()

    def get_element_locator(self):
        """Element position on page"""
        return self._find_by_locator().locator

    def get_parent(self):
        """Wrapper for Web Element parent property"""
        return self._find_by_locator().parent

    def get_element(self, by, criteria):
        # Need reuse criteria
        """IF we are searching by Any strategy ==> By.CSS_SELECTOR, value """
        return self._find_by_locator().find_element(by, criteria)

    def get_elements(self, by, criteria):
        # Need reuse criteria
        """IF we are searching by Any strategy ==> By.CSS_SELECTOR, value """
        return self._find_by_locator().find_elements(by, criteria)

    def get_attribute(self, item):
        return self._find_by_locator().get_attribute(item)

    def _find_by_locator(self):
        try:
            return self.driver.find_element(By.CSS_SELECTOR, self.locator)
        except Exception:
            return self.driver.find_element(By.XPATH, self.locator)

    def _find_all_by_locator(self):
        try:
            return self.driver.find_elements(By.CSS_SELECTOR, self.locator)
        except Exception:
            return self.driver.find_elements(By.XPATH, self.locator)
