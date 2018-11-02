from selene.support.jquery_style_selectors import s


class BaseWidget:

    def __init__(self, locator):
        self.root = s(locator)

    def is_open(self):
        return self.root.is_displayed()
