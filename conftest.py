import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    url = "https://www.amazon.com.tr"
    driver = webdriver.Safari()
    driver.cleanSession = True
    driver.ensureCleanSession = True
    driver.delete_all_cookies()
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.close()