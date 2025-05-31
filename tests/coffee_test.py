import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))



import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_coffee_name_immutable():
    c = Coffee("Latte")
    assert c.name == "Latte"
    with pytest.raises(AttributeError):
        c.name = "Cappuccino"

def test_coffee_orders_customers():
    c = Coffee("Latte")
    cust1 = Customer("Rico")
    cust2 = Customer("Alex")

    cust1.create_order(c, 5.0)
    cust2.create_order(c, 7.0)

    assert len(c.orders()) == 2
    assert set(c.customers()) == {cust1, cust2}

def test_coffee_aggregates():
    c = Coffee("Latte")
    cust = Customer("Rico")

    assert c.num_orders() == 0
    assert c.average_price() == 0

    cust.create_order(c, 5.0)
    cust.create_order(c, 7.0)

    assert c.num_orders() == 2
    assert c.average_price() == 6.0
