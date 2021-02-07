import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def browser(request):
    print("\nstart browser for test..")

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': 'http://selenium1py.pythonanywhere.com/{prefs}/catalogue/coders-at-work_207/'})
    user_language = request.config.getoption("language")
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()