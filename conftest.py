import pytest
from selenium import webdriver

@pytest.fixture(scope='function',params=['chrome','firefox'])
def driver(request):
    global driver
    if request.param == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        driver = webdriver.Chrome(options=options)
    elif request.param == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument('--start-maximized')
        driver = webdriver.Firefox(options=options)

    yield driver
    driver.quit()