from src.ui.elements.button import Button
from src.ui.widgets.app_drawer.app_darwer_widget import AppDrawer
from src.ui.widgets.settings.controls_widget import Controls



class Header:
    _settings_btn_locator = "[id='SettingsDrawer_Trigger_Button']"
    _app_drawer_btn_locator = "[id='AppDrawer_Trigger_Button']"

    def __init__(self):
        self.settings_btn = Button(self._settings_btn_locator)
        self._app_drawer_btn = Button(self._app_drawer_btn_locator)

    def open_controls(self):
        self.settings_btn.click()
        return Controls()

    def open_app_drawer(self):
        self._app_drawer_btn.click()
        return AppDrawer()
