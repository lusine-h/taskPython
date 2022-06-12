from lib2to3.pgen2 import driver
import pytest
from basePage.base_page import Base
from page.greenkart import GreenKart_elemets

@pytest.mark.usefixtures('set_up')
class Test_greenKart():

    def test_page_title(self, set_up):
        check = GreenKart_elemets(driver)
        actual_page_url = check.page_title_url(self)
        expected_page_url = ("GreenKart - veg and fruits kart", "https://rahulshettyacademy.com/seleniumPractise/#/")
        assert actual_page_url == expected_page_url

    def test_buy_mango(self,set_up):
        check = GreenKart_elemets(driver)
        check.add_mango_to_cart()

        actual_item = check.items_num()
        actual_price = check.price_num()
        expected_item = ("Items	:	1")
        expected_price = ("Price	:	75")
        assert actual_item == expected_item
        assert actual_price == expected_price

        check.open_cart()
        assert check.open_cart()== True

        actual_prod = check.cart_products()
        expected_prod = ("1 No.")
        assert actual_prod == expected_prod

        check.proceed()
        assert check.proceed() == True

        check.cart_page()
        assert check.cart_page == True

        actual_num = check.num_of_items()
        expected_num = ("1")
        assert actual_num == expected_num

        check.palce_an_order()
        assert check.palce_an_order()== True

        check.terms_and_conditions()
        assert check.terms_and_conditions() == True

        check.proceed_2()
        assert check.proceed_2() == True

        check.success_message()
        assert check.success_message == True