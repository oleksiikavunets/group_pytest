from selene.support.jquery_style_selectors import s

from src.ui.elements.button import Button
from src.ui.widgets.app_drawer.app_selector_widget import AppSelector
from src.ui.widgets.app_drawer.profile_widget import Profile


class AppDrawer:
    _root_selector = '[class^="appDrawer"]'
    _profile_btn_selector = "[class^='expandArea']"

    def __init__(self):
        self.profile_btn = Button(self._profile_btn_selector)

    def is_open(self):
        return "Open" in s(self._root_selector).get_attribute("class")

    def open_profile_area(self):
        self.profile_btn.click()
        return Profile()

    def open_app_selector(self):
        return AppSelector()
