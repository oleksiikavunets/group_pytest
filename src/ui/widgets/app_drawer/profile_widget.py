from src.ui.widgets.app_drawer.profile.profile_controls import ProfileMenu


class Profile:
    _profile_button_locator = "[class='']"

    def open_profile_menu(self):
        return ProfileMenu()
