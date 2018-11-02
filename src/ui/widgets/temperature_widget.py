from src.ui.elements.button import Button


class TemperatureControlls:
    _temperature_btn_locator = "[class='temperature-2DEjG']"

    def __init__(self):
        self.appDrawer_ = Button(self._settings_tub_locator)