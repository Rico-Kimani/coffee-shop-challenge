import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))



import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_order_initialization_and_properties():
    customer = Customer("Rico")
    coffee = Coffee("Mocha")
    order = Order(customer, coffee, 6.5)

    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 6.5

    with pytest.raises(Exception):
        Order("not_customer", coffee, 5.0)

    with pytest.raises(Exception):
        Order(customer, "not_coffee", 5.0)

    with pytest.raises(Exception):
        Order(customer, coffee, 0.5)

    with pytest.raises(Exception):
        order.price = 10.0  # Should raise AttributeError or similar
