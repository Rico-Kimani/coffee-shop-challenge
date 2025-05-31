from customer import Customer
from coffee import Coffee
from order import Order

alice = Customer("Alice")
latte = Coffee("Latte")

order1 = alice.create_order(latte, 4.5)
order2 = alice.create_order(latte, 5.0)

print(alice.orders())
print(latte.num_orders())
print(latte.average_price())
