from selene import browser
from selenium.webdriver.common.by import By

from src.ui.elements.button import Button
from src.ui.widgets.app_drawer.app_drawer_widget import AppDrawer
from src.ui.widgets.settings.controls_widget import Controls


class Header:
    _settings_btn_locator = "//*[@id='SettingsDrawer_Trigger_Button']"
    _app_drawer_btn_locator = "[id='AppDrawer_Trigger_Button']"

    def __init__(self, driver):
        self.driver = driver
        self.settings_btn = Button(self.driver, self._settings_btn_locator)
        self.app_drawer_btn = Button(self.driver, self._app_drawer_btn_locator)

    def open_controls(self):
        self.driver.find_element(By.XPATH,  self._settings_btn_locator).click()
        # self.settings_btn.click()
        return Controls()

    def click_app_drawer(self):
        self.app_drawer_btn.click()
        return AppDrawer()
