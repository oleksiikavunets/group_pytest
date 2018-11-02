from src.ui.elements.base_element import BaseElement


class Button(BaseElement):

    def __init__(self, driver,  locator):
        super().__init__(driver, locator)

    def click(self):
        self._find_by_locator().click()

    def get_name(self):
        self._find_by_locator().text
