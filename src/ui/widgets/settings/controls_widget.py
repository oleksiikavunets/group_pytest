from src.ui.elements.button import Button
from src.ui.widgets.settings.settings_widget import Settings


class Controls:
    _settings_tub_locator = "[id='SettingsDrawerHeader_Settings_Button']"
    _drive_modes_btn_locator = "[id='QuickControls_DriveModes_Button']"

    def __init__(self):
        self.settings_tub = Button(self._settings_tub_locator)
        self.drive_modes_btn = Button(self._drive_modes_btn_locator)

    def click_settings_tub(self):
        return Settings()