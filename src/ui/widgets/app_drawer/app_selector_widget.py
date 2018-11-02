from src.ui.elements.button import Button


def defineAppsLength(self):
    pass

class AppSelector:
    _app_news_button_locator = ".buttonCircularText'[value='News']"
    _app_phone_button_locator = ".buttonCircularText'[value='Phone']"
    _app_navig_button_locator = ".buttonCircularText'[value='Navigation']"
    _app_radio_button_locator = ".buttonCircularText'[value='Radio']"
    _app_media_button_locator = ".buttonCircularText'[value='Media']"
    _app_widgets_button_locator = ".buttonCircularText'[value='Widgets']"

    def __init__(self, _app_list_length):
        self.news_butt = Button(self._app_news_button_locator)
        self._app_phone_button_locator = Button(self._app_phone_button_locator)
        self._app_navig_button_locator = Button(self._app_navig_button_locator)
        self._app_radio_button_locator = Button(self._app_radio_button_locator)
        self._app_media_button_locator = Button(self._app_media_button_locator)
        self._app_widgets_button_locator = Button(self._app_widgets_button_locator)
