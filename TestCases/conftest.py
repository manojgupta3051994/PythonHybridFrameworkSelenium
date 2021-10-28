from selenium import webdriver
import pytest

@pytest.fixture()
def setUp(browser):
    if browser == 'chrome':
        print ("****Launching Chrome*********")
        driver = webdriver.Chrome(executable_path=r'C:\Users\Manoj\Desktop\Python - Selenium Practice\Drivers\chromedriver.exe')
    elif browser == 'firefox':
        print ("****Launching Firefox*********")
        driver = webdriver.Firefox(executable_path=r'C:\Users\Manoj\Desktop\Python - Selenium Practice\Drivers\geckodriver.exe')
    else:
        print ("****Launching IE*********")
        driver = webdriver.Ie()
    return driver


def pytest_addoption(parser):
    parser.addoption('--browser')

@pytest.fixture()
def browser(request):
    return request.config.getoption('--browser')


def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Person'] = 'Manoj'

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop('Plugins',None)