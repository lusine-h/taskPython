import pytest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

@pytest.fixture(autouse=True)
def test_setup():
    path = Service('driver/chromedriver.exe')
    driver = webdriver.Chrome(service=path)
    driver.implicitly_wait(10)
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
    driver.maximize_window()
    yield driver
    if driver is not None:
        driver.close()
        driver.quit()



