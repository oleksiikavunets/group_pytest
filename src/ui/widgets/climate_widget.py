from src.ui.widgets.climate.climate_menu_widget import ClimateMenu


class Climate:
    _locator = ""

    def __init__(self, driver):
        self.driver = driver

    def open_climate_menu(self):
        return ClimateMenu(self.driver)
