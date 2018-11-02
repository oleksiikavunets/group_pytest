from src.ui.elements.button import Button


class ProfileMenu:

    _profile_btn_locator = "[class^='profileContent']"
    _profile_heading_locator = "[class^='profileHeading']"
    _profile_recomend_area_locator = "[class^='recommendationArea']"

    def __init__(self):
        self.profile_btn = Button(self._profile_btn_locator)
        ##