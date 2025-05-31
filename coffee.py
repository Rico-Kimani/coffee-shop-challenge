class Coffee:
    def __init__(self, name):
        self.name = name  # calls setter

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if len(value) < 3:
            raise ValueError("Name must be at least 3 characters")
        if hasattr(self, '_name'):
            raise AttributeError("Coffee name cannot be changed after initialization")
        self._name = value

    def orders(self):
        from order import Order
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
        # Return unique customers who ordered this coffee
        return list({order.customer for order in self.orders()})
    
    def num_orders(self):
        # Number of orders for this coffee
        return len(self.orders())
    
    def average_price(self):
        orders = self.orders()
        if not orders:
            return 0.0
        return sum(order.price for order in orders) / len(orders)
