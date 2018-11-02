import allure
from delayed_assert import expect, assert_expectations

from src.ui.pages.app_page import AppPage


@allure.feature("App_Drawer")
class TestAppDrawer:
    def test_app_drawer_1(self):

        app = AppPage(self.driver).open_page()

        expect(app.header.settings_btn.is_displayed())
        expect(app.header.app_drawer_btn.is_displayed())

        app_drawer = app.header.click_app_drawer()
        expect(app_drawer.is_open())

        app.header.click_app_drawer()

        expect(not app_drawer.is_open())

        assert_expectations()




    def test_app_drawer_2(self):
        pass

    def test_app_drawer_3(self):
        pass

    def test_app_drawer_4(self):
        pass

    def test_app_drawer_5(self):
        pass
