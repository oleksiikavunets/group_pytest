from selene import browser

from src.ui.widgets.climate_widget import Climate
from src.ui.widgets.header_widget import Header


class AppPage:
    def __init__(self):
        self.header = Header()
        self.climate = Climate()

    def open_page(self):
        browser.open_url('/')
        return self
