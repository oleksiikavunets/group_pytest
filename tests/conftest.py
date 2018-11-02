import allure
import pytest
from allure_commons.types import AttachmentType
from selene import config, browser
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def setup_session():
    config.base_url = "http://172.31.239.134:8000/menlo-center-stack/"
    config.reports_folder = 'reports'
    config.start_maximized = 'True'
    # config.browser_name = 'chrome'

    browser.set_driver(webdriver.Chrome(ChromeDriverManager().install()))
    yield
    browser.driver().quit()


# def pytest_exception_interact(node, call, report):
#     print("\nTEST FAILED IN !!!!!!!!!!!!!!!!")
#     attach = browser.driver().get_screenshot_as_png()
#     allure.attach(attach, name="Screenshot", attachment_type=AttachmentType.PNG)
