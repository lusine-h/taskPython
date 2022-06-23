from lib2to3.pgen2 import driver
from locators.locators import LocatorsXpath
import selenium
import pytest
from selenium.webdriver.common.by import By
from page.conftest import test_setup


class GreenKart_elemets(LocatorsXpath):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver
 
    def page_title_url(self,driver):
        driver = self.driver
        page_title = driver.title
        page_url = driver.current_url
        return page_title, page_url

    def find_mango(self):
        mango_btn = self.driver.find_element(By.XPATH,LocatorsXpath.mango)
        mango_btn.click()
        status = mango_btn.is_selected()
        print(status)
    
    def add_mango_to_cart(self):
        add_cart= self.driver.find_element(By.XPATH,LocatorsXpath.add_to_cart)
        add_cart.click()
        status = add_cart.is_selected()
        print(status)

    def items_num(self):
        mango_items = self.driver.find_element(By.XPATH,LocatorsXpath.items)
        return mango_items.text

    def price_num(self):
        mango_price = self.driver.find_element(By.XPATH,LocatorsXpath.price)
        return mango_price.text

    def open_cart(self):
        open_cart_btn = self.driver.find_element(By.XPATH,LocatorsXpath.cart)
        open_cart_btn.click()
        status = open_cart_btn.is_selected()
        print(status)

    def cart_products(self):
        prods_cart = self.driver.find_element(By.XPATH,LocatorsXpath.product_in_cart)
        prods_cart.is_displayed()
        return prods_cart.text

    def proceed(self):
        proceed_btn = self.driver.find_element(By.XPATH,LocatorsXpath.proceed)
        proceed_btn.click()
        status = proceed_btn.is_selected()
        print(status)

    def cart_page(self):
        driver= self.driver
        cart_page_title = driver.title
        cart_page_url = driver.current_url
        return cart_page_title, cart_page_url

    def num_of_items(self):
        num_of_items =self.driver.find_element(By.XPATH,LocatorsXpath.number_of_items)
        return num_of_items.text

    def palce_an_order(self):
        order_btn = self.driver.find_element(By.XPATH,LocatorsXpath.place_order)
        order_btn.click()
        status = order_btn.is_selected()
        print(status)

    def terms_conditions(self):
        checkbox = self.driver.find_element(By.XPATH,LocatorsXpath.terms_and_conditions)
        checkbox.click()
        status = checkbox.is_selected()
        print(status)

    def proceed_2(self):
        proceed_2btn = self.driver.find_element(By.XPATH,LocatorsXpath.proceed_2)
        proceed_2btn.click()
        status = proceed_2btn.is_selected()
        print(status)
        
    def message(self):
       success_message = self.driver.find_element(By.XPATH,LocatorsXpath.success_message)
       status = success_message.is_displayed()
       print(status)

       
