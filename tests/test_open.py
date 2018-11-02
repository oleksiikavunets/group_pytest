from src.ui.pages.app_page import AppPage


def test_can_open():
    # pass
    app = AppPage().open_page()
    controls = app.header.open_controls()
    controls.click_settings_tub()