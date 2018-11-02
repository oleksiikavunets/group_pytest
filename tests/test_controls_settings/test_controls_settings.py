import allure
from selene import browser, config

from src.ui.pages.app_page import AppPage
from tests.test_controls_settings.contols_settings_base_test import ControlsSettingsBaseTest


# @allure.feature("Controls_Settings")
class TestControlsSettings:

    # def before(self):
    #     super(TestControlsSettings, self).before()
    #
    # def after(self):
    #     super(TestControlsSettings, self).after()

    # @allure.testcase("", 'Test case title')
    def test_control_drawer_1(self):
        app = AppPage().open_page()
        controls = app.header.open_controls()

    def test_control_drawer_2(self):
        pass

    def test_control_drawer_3(self):
        pass
