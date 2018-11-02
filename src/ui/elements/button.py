from src.ui.elements.base_element import BaseElement


class Button(BaseElement):

    def __init__(self, locator):
        super().__init__(locator)

    def click(self):
        self.element.click()

    def get_name(self):
        self.element.text
