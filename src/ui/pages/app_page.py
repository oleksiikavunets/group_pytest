from src.ui.widgets.climate_widget import Climate
from src.ui.widgets.header_widget import Header


class AppPage:
    def __init__(self, driver):
        self.driver = driver
        self.header = Header(self.driver)
        self.climate = Climate(self.driver)

    def open_page(self):
        self.driver.get('http://172.31.239.134:8000/menlo-center-stack/')
        return self
