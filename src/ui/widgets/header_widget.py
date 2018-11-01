from src.ui.widgets.app_darwer_widget import AppDrawer
from src.ui.widgets.settings.controls_widget import Controls



class Header:
    def open_controls(self):
        return Controls()

    def open_app_drawer(self):
        return AppDrawer()