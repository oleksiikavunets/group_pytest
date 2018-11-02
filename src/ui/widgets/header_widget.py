import time

from selene import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait as wait

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
        return Controls(self.driver)


    def open_app_drawer(self):
        self.app_drawer_btn.click()
        return AppDrawer(self.driver)

    def close_app_drawer(self):
        self.app_drawer_btn.click()
        # wait(self.driver, 30).until(lambda x: not AppDrawer(self.driver).is_open())

