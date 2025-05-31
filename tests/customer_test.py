import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_customer_name_getter_setter():
    c = Customer("Rico")
    assert c.name == "Rico"

    c.name = "Sam"
    assert c.name == "Sam"

    with pytest.raises(Exception):
        c.name = ""

    with pytest.raises(Exception):
        c.name = "A" * 16

def test_customer_orders_and_coffees():
    c = Customer("Rico")
    coffee1 = Coffee("Latte")
    coffee2 = Coffee("Espresso")
    
    c.create_order(coffee1, 5.5)
    c.create_order(coffee2, 4.0)
    c.create_order(coffee1, 6.0)

    assert len(c.orders()) == 3
    assert set(c.coffees()) == {coffee1, coffee2}
