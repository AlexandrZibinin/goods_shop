import pytest
from Classes import Category, Product

@pytest.fixture()
def category_object():
    return Category('parts', 'parts for warhouse tracks', ['wheel', 'oil', 'filter'])
@pytest.fixture()
def product_object():
    return Product('red wheel', 'round', 1000.00, 10)

def test_init_category(category_object):
    assert category_object.name == 'parts'
    assert category_object.description == 'parts for warhouse tracks'
    assert category_object.goods == ['wheel', 'oil', 'filter']

def test_init_product(product_object):
    assert product_object.name == 'red wheel'
    assert product_object.description == 'round'
    assert product_object.price == 1000.00
    assert product_object.quantity_in_stock == 10
    assert product_object.total_categories == 0
    assert product_object.total_unique_products == 0
