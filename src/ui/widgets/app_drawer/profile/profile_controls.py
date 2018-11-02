from src.ui.elements.button import Button


class ProfileMenu:
    _profile_btn_locator = "[class^='profileContent']"
    _arrow_button_closed = "[class^='chevronClosed']"
    _arrow_button_opened = "[class^='chevronOpened']"
    _profile_heading_locator = "[class^='profileHeading']"
    _profile_recomend_area_locator = "[class^='recommendationArea']"

    def __init__(self):
        self.profile_btn = Button(self._profile_btn_locator)
        self.arrow_btn = Button(self._arrow_button_closed)

    def open_profiles(self):
        self.arrow_btn.click()
        self.arrow_btn = Button(self._arrow_button_opened)

    def close_profiles(self):
        self.arrow_btn.click()
        self.arrow_btn = Button(self._arrow_button_closed)
