from src.ui.elements.base_element import BaseElement


class Button(BaseElement):

    def __init__(self, driver,  locator):
        super().__init__(driver, locator)

    def click(self):
        self.element.click()

    def get_name(self):
        self.element.text
