from selene import browser

from src.ui.elements.base_element import BaseElement
import selene.support.by
from selene.support.jquery_style_selectors import s
from src.ui.elements.button import Button


class ContentWidget(BaseElement):


    """PageWidgets Base class and their helper methods. This class accepts
    driver and web locator from the locators package as inputs
       //*[contains(@class, 'settings-section-2_')] shows all available widgets"""
    def __init__(self, locator):
        section_common_path = "//*[contains(@class, 'settings-section-2_')]"

        if isinstance(locator, int):
            locator = format("(%s)[%s]", section_common_path, locator)
        if locator.startswith("name="):
            name = locator.split(locator, "=")[1]
            locator = format(
                "%s//*[contains(@class,'section-header') and contains(.,'%s')]/parent::*", section_common_path, name
            )

        super().__init__(locator)

    """Actually scrolls to element  via JS"""
    def scroll_to_element(self):
        browser.execute_script("arguments[0].scrollIntoView();", self.element)

    def get_name(self):
        return self.element.find_element(selene.xpath, "//*[contains(@class,'section-header')]").text

    def get_section(self, criteria):
        # return Section(criteria)
        pass

    def get_all_sections(self):
        return self.get_elements(selene.xpath, "//*[contains(@class, 'Container')]//*[contains(@class,'Section']")

    def get_button(self, locator=None):
        if locator is None:
            return Button(self.get_element_locator() + "//*[contains(@id, 'button')]")
        if isinstance(locator, int):
            return self.get_buttons()[locator]
        else:
            return Button(self.get_element_locator() + locator)

    def get_buttons(self):
        return self.get_elements("//*[contains(@id, 'button')]");

