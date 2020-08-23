import pytest
from pages import amazon_page, flipkart_page


def price_comparer():
    amazon_price = amazon_page.amazon().amazon()
    flipkart_price = flipkart_page.flipkart_class().flipkart_short_cut()

    if flipkart_price > amazon_price:
        print('Buy it From Amazon')
    elif flipkart_price < amazon_price:
        print('Buy it From Flipkart')
    else:
        print('Buy it from Either')


price_comparer()
