import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language of browser interface")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")

    if user_language == None:
        raise pytest.UsageError("--language should be defined")
    else:
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        print("\nStart Chrome browser for test..")
        browser = webdriver.Chrome(options=options)
        yield browser
        print("\nQuit")
    