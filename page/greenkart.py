from lib2to3.pgen2 import driver
from locators.locators import LocatorsXpath
import selenium
import pytest

class GreenKart_elemets(LocatorsXpath):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver
 
    def page_title_url(self):
        driver = self.driver
        page_title = driver.title
        page_url = driver.current_url
        return page_title, page_url

    def find_mango(self):
        mango_btn = self.driver.find_element_by_xpath(LocatorsXpath.mango)
        mango_btn.click()
        status = mango_btn.is_selected()
        print(status)
    
    def add_mango_to_cart(self):
        add_cart= self.driver.find_element_by_xpath(LocatorsXpath.add_to_cart)
        add_cart.click()
        status = add_cart.is_selected()
        print(status)

    def items_num(self):
        mango_items = self.driver.find_element_by_xpath(LocatorsXpath.items)
        mango_items.equals("Items	:	1")
        return mango_items

    def price_num(self):
        mango_price = self.driver.find_element_by_xpath(LocatorsXpath.price)
        mango_price.equals("Price	:	75")
        return mango_price

    def open_cart(self):
        open_cart_btn = self.driver.find_element_by_xpath(LocatorsXpath.cart)
        open_cart_btn.click()
        status = open_cart_btn.is_selected()
        print(status)

    def cart_products(self):
        prods_cart = self.driver.find_element_by_xpath(LocatorsXpath.product_in_cart)
        prods_cart.is_displayed()
        prods_cart.equals("1 No.")

    def proceed(self):
        proceed_btn = self.driver.find_element_by_xpath(LocatorsXpath.proceed)
        proceed_btn.click()
        status = proceed_btn.is_selected()
        print(status)

    def cart_page(self):
        driver= self.driver
        cart_page_title = driver.title
        cart_page_url = driver.current_url
        return cart_page_title, cart_page_url

    def num_of_items(self):
        num_of_items =self.driver.find_element_by_xpath(LocatorsXpath.number_of_items)
        num_of_items.equals("1")
        return num_of_items

    def palce_an_order(self):
        order_btn = self.driver.find_element_by_xpath(LocatorsXpath.place_order)
        order_btn.click()
        status = order_btn.is_selected()
        print(status)

    def terms_conditions(self):
        checkbox = self.driver.find_element_by_xpath(LocatorsXpath.terms_and_conditions)
        checkbox.click()
        status = checkbox.is_selected()
        print(status)

    def proceed_2(self):
        proceed_2btn = self.driver.find_element_by_xpath(LocatorsXpath.proceed_2)
        proceed_2btn.click()
        status = proceed_2btn.is_selected()
        print(status)
        
    def message(self):
       success_message = self.driver.find_element_by_xpath(LocatorsXpath.success_message)
       status = success_message.is_displayed()
       print(status)

       
