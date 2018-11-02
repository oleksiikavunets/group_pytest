import allure

from tests.controls_settings.contols_settings_base_test import ControlsSettingsBaseTest


@allure.feature("Controls_Settings")
class TestControlsSettings(ControlsSettingsBaseTest):

    def before(self):
        super(TestControlsSettings, self).before()

    def after(self):
        super(TestControlsSettings, self).after()

    @allure.testcase("", 'Test case title')
    def test_control_drawer_1(self):
        print('a')

    def test_control_drawer_2(self):
        pass

    def test_control_drawer_3(self):
        pass
