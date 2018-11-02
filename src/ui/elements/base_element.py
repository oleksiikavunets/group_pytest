from selene.support.jquery_style_selectors import s


class BaseElement(object):

    def __init__(self, locator):
        self.element = s(locator)

    def is_enabled(self):
        """"""
        return self.web_element.is_enabled()

    def is_displayed(self):
        """Wrapper for Web Element is_displayed Method"""
        return self.element.is_displayed()

    def is_selected(self):
        """"""
        return self.element.is_selected()

    def get_element_locator(self):
        """Element position on page"""
        return self.element.locator

    def get_parent(self):
        """Wrapper for Web Element parent property"""
        return self.element.parent

    def get_element(self, by, criteria):
        # Need reuse criteria
        """IF we are searching by Any strategy ==> By.CSS_SELECTOR, value """
        return self.element.find_element(by, criteria)

    def get_elements(self, by, criteria):
        # Need reuse criteria
        """IF we are searching by Any strategy ==> By.CSS_SELECTOR, value """
        return self.element.find_elements(by, criteria)

    def get_attribute(self, item):
        return self.element.get_attribute(item)
