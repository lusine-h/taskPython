import pytest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

class Base:
    @pytest.fixture(autouse=True)
    def test_setup(self):
        self.driver = webdriver.Chrome('C:/Users/lhovh/OneDrive/Documents/chromedriver.exe')
        self.driver.implicitly_wait(10)
        self.driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
        self.driver.maximize_window()

        yield self.driver
        if self.driver is not None:
            self.driver.close()
            self.driver.quit()
