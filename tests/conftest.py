import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def setup_session(request):
    web_driver = webdriver.Chrome(ChromeDriverManager().install())

    web_driver.maximize_window()
    session = request.node
    for item in session.items:
        cls = item.getparent(pytest.Class)
        setattr(cls.obj, "driver", web_driver)
    yield web_driver
    web_driver.quit()


# def pytest_exception_interact(node, call, report):
#     print("\nTEST FAILED IN !!!!!!!!!!!!!!!!")
#     attach = browser.driver().get_screenshot_as_png()
#     allure.attach(attach, name="Screenshot", attachment_type=AttachmentType.PNG)
