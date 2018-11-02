import pytest
from selene import config


@pytest.fixture(scope="session")
def setup_session():
    config.browser_name = 'chrome'
    config.reports_folder = 'reports'
    config.base_url = "http://172.31.239.134:8000/menlo-center-stack"
