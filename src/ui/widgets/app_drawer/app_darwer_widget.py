from src.ui.widgets.app_drawer.app_selector_widget import AppSelector
from src.ui.widgets.app_drawer.profile_widget import Profile


class AppDrawer:

    def open_profile_area(self):
        return Profile()

    def open_app_selector(self):
        return AppSelector()