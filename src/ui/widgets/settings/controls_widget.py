from selene.support.jquery_style_selectors import s

from src.ui.elements.button import Button
from src.ui.widgets.base_widget import BaseWidget
from src.ui.widgets.settings.settings_widget import Settings


class Controls(BaseWidget):

    _settings_tub_locator = "[id='SettingsDrawerHeader_Settings_Button']"
    _drive_modes_btn_locator = "[id='QuickControls_DriveModes_Button']"
    _driver_assist_btn_locator = "[id='QuickControls_DriverAssist_Button']"
    _valet_mode_btn_locator = "[id='QuickControls_ValetMode_Button']"
    _doors_lock_btn_locator = "[id='QuickControls_DoorsLocks_Button']"
    _root_locator = "[class*='settingsAreaWrapper']"

    """drive modes"""
    _drive_mode_normal_btn_locator = "[src*='iconDriveModeNormal']"
    _drive_mode_sport_btn_locator = "[src*='iconDriveModeSport']"
    _drive_mode_eco_btn_locator = "[src*='iconDriveModeEco']"
    _drive_mode_slippery_btn_locator = "[src*='iconDriveModeSlippery']"
    _drive_mode_pedal_btn_locator = "[src*='iconDriveModePedal']"

    """frunk trunk"""
    _hood_btn_locator = "[class*='hood-icon']"
    _trunk_btn_locator = "[class*='trunk-icon']"

    def __init__(self):
        super().__init__(self._root_locator)
        self.settings_tub = Button(self._settings_tub_locator)
        self.drive_modes_btn = Button(self._drive_modes_btn_locator)
        self.doors_lock_btn = Button(self._doors_lock_btn_locator)
        self.driver_assist_btn = Button(self._driver_assist_btn_locator)
        self.valet_mode_btn = Button(self._valet_mode_btn_locator)

        self.drive_mode_normal_btn = Button(self._drive_mode_normal_btn_locator)
        self.drive_mode_sport_btn = Button(self._drive_mode_sport_btn_locator)
        self.drive_mode_eco_btn = Button(self._drive_mode_eco_btn_locator)
        self.drive_mode_slippery_btn = Button(self._drive_mode_slippery_btn_locator)
        self.drive_mode_pedal_btn = Button(self._drive_mode_pedal_btn_locator)

    def click_settings_tub(self):
        self.settings_tub.click()
        return Settings()