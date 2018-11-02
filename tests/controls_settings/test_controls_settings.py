import allure
import time

import pytest
from selene import browser, config

from src.ui.pages.app_page import AppPage
from tests.controls_settings.contols_settings_base_test import ControlsSettingsBaseTest


# @allure.feature("Controls_Settings")
class TestControlsSettings(ControlsSettingsBaseTest):

    @pytest.fixture(scope="function", autouse=True)
    def before(self):
        super(TestControlsSettings, self).before()
        print('a')

    @pytest.yield_fixture(scope="function", autouse=True)
    def after(self):
        super(TestControlsSettings, self).after()
        print('b')

    @allure.testcase("https://testrail.ford.com/index.php?/cases/view/test_case_id")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_control_drawer_1(self):

        app = AppPage().open_page()
        controls = app.header.open_controls()
        controls.click_settings_tub()

    def test_control_drawer_2(self):
        pass

    def test_control_drawer_3(self):
        pass
