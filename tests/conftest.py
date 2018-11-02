import allure
import pytest
from allure_commons.types import AttachmentType
from selene import config, browser


@pytest.fixture(scope="session")
def setup_session():
    config.browser_name = 'chrome'
    config.reports_folder = 'reports'
    config.base_url = "http://127.0.0.1:8000/menlo-center-stack"


def pytest_exception_interact(node, call, report):
    print("\nTEST FAILED IN !!!!!!!!!!!!!!!!")
    attach = browser.driver().get_screenshot_as_png()
    allure.attach(attach, name="Screenshot", attachment_type=AttachmentType.PNG)
