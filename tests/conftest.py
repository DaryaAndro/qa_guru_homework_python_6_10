import pytest
import os
import tests
from selene import browser


# Путь до директории resources
def path(file_name):
    return os.path.abspath(os.path.join(os.path.dirname(tests.__file__), f'resources/{file_name}'))


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    # browser.config.timeout = 6.0

    yield

    browser.quit()
