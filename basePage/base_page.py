from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
import pytest

@pytest.fixture(autouse=True)
def set_up(self):
        path = 'driver/chromedriver.exe'
        self.driver = webdriver.Chrome(executable_path = path)
        self.driver.implicitly_wait(10)
        self.driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
        self.driver.maximize_window()

        yield self.driver
        if self.driver is not None:
            self.driver.close()
            self.driver.quit()
