from src.ui.pages.app_page import AppPage


def test():
    app = AppPage()
    controls = app.header.open_controls()
    controls.drive_modes_btn.click()
    settings = controls.click_settings_tub()
    app_drawer = app.header.open_app_drawer()