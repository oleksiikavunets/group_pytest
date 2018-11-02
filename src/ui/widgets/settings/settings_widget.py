from src.ui.elements.button import Button


class Settings:
    _display_btn_locator = "[id='Settings_Display_Button']"
    _sound_btn_locator = "[id='Settings_Sound_Button']"
    _clock_btn_locator = "[id='Settings_Clock_Button']"
    _audio_btn_locator = "[id='Settings_Audio_Button']"
    _phone_btn_locator = "[id='Settings_Phone_Button']"
    _vehicle_btn_locator = "[id='Settings_Vehicle_Button']"
    _driver_assist_btn_locator = "[id='Settings_DriverAssist_Button']"
    _language_btn_locator = "[id='Settings_Language_Button']"
    _develop_btn_locator = "[id='Settings_Developer_Button']"

    def __init__(self):
        self.display_btn = Button(self._display_btn_locator)
        self.sound_btn = Button(self._sound_btn_locator)
        self.clock_btn = Button(self._clock_btn_locator)
        self.audio_btn = Button(self._audio_btn_locator)
        self.phone_btn = Button(self._phone_btn_locator)
        self.vehicle_btn = Button(self._vehicle_btn_locator)
        self.driver_assist_btn = Button(self._driver_assist_btn_locator)
        self.language_btn = Button(self._language_btn_locator)
        self.develop_btn = Button(self._develop_btn_locator)
