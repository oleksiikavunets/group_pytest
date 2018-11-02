from selene import config


def set_up():
    config.browser_name = 'chrome'
    config.reports_folder = 'reports'
    config.base_url = "http://172.31.239.134:8000/menlo-center-stack/"
