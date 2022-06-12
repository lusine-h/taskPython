import selenium 

class LocatorsXpath: 
    mango = '//*[@id="root"]/div/div[1]/div/div[18]/div[1]/img'
    add_to_cart = '//*[@id="root"]/div/div[1]/div/div[18]/div[3]/button'
    items = '//*[@id="root"]/div/header/div/div[3]/div[1]/table/tbody/tr[1]/td[3]/strong'
    price ='//*[@id="root"]/div/header/div/div[3]/div[1]/table/tbody/tr[2]/td[3]/strong'
    cart ='//*[@id="root"]/div/header/div/div[3]/a[4]/img'
    product_in_cart = '//*[@id="root"]/div/header/div/div[3]/div[2]/div[1]/div[1]/ul/li/div[2]/p[1]'
    proceed = '//*[@id="root"]/div/header/div/div[3]/div[2]/div[2]/button'
    cart_page ='//*[@id="root"]/div/div/div'
    number_of_items = '//*[@id="productCartTables"]/tbody/tr/td[3]/p'
    place_order = '//*[@id="root"]/div/div/div/div/button'
    terms_and_conditions ='//*[@id="root"]/div/div/div/div/input'
    proceed_2 = '//*[@id="root"]/div/div/div/div/button'
    success_message = "//*[contains(text(), 'Thank you, your order has been placed successfully')]"
