from src.ui.pages.app_page import AppPage
from delayed_assert import expect, assert_expectations


def test():
    app = AppPage().open()
    controls = app.header.open_controls()
    settings = controls.click_settings_tub()
    expect(1==3)
    app_drawer = app.header.open_app_drawer()
    expect(2==2)
    expect(2==5)
    expect(2==2)
    assert_expectations()
