import pytest
from pages import amazon_page, flipkart_page

@pytest.mark.flipkart_price
def get_flipkart_price():
    assert flipkart_page.flipkart_class().flipkart_short_cut(), 'Unable To Retrive'


@pytest.mark.amazon_price
def get_amazon_price():
    assert amazon_page.amazon().amazon(), 'Unable To Retrive'