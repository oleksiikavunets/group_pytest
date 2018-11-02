from src.ui.elements.button import Button


def defineAppsLength(self):
    pass

class AppSelector:
    _app_list_locator = "[class^='gridItem']"
    _app_list_lenght = 0

    def __init__(self, _app_list_length):
        defineAppsLength(self)
        for i in range(_app_list_length):
            self.appSelector_ = Button(self._app_list_locator)
