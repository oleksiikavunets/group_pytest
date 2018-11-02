from src.ui.elements.base_element import BaseElement


class Widget(BaseElement):
    """PageWidgets Base class and their helper methods. This class accepts
    driver and web locator from the locators package as inputs
       //*[contains(@class, 'settings-section-2_')] shows all available widgets"""
    def __init__(self, page, widget_locator):
        # self._page = page
        # self.driver = page.driver
        # self.widget_locator = widget_locator
        #TODO: think about that
        # self.web_element = self.driver.get_element(page, widget_locator)
        #
        #self.driver.execute_script("arguments[0].scrollIntoView();", self.web_element)

        #self.touch_actions = TouchActions(self.driver)
        #self.action_chains = ActionChains(self.driver)
        # Scroll to the element




    def get_text(self):
        """Wrapper for Web Element text property"""
        #return self.web_element.find_element(By.XPATH, "(//*[contains(@class,'section-header')])[0]").text


    #TODO: Name or Path or Number
    def get_section(self, criteria, by=None):
        basicXpath = format("//*[contains(@class, 'Container')]//*[contains(@class,'Section' contains(., '%s')]", criteria)
        #Need reuse criteria
        # if by is not None:
        #     return self.web_element(by, criteria)
        # if isinstance(criteria, int):
        #     return self.get_all_sections()[criteria]
        # if criteria.startswith("//") or criteria.startswith("./"):
        #     return self.web_element.find_element(By.XPATH, criteria)
        # else:
        #     return self.web_element.find_element(By.XPATH, basicXpath)

    def get_all_sections(self):
        # return self.web_element.find_elements(By.XPATH, "//*[contains(@class, 'Container')]//*[contains(@class,'Section']")
        pass

    #TODO: Button without Section -->
    def get_button(self):
        return ######

    def get_buttons(self):
        return ######

    #TODO: return buttons - Can Be Slider (Radio Button - On/Off  --> IsEnabled/Disabled)
    #TODO: Can be  SliderTumb
