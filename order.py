class Order:
    all = []

    def __init__(self, customer, coffee, price: float):
        from customer import Customer
        from coffee import Coffee

        if not isinstance(price, float):
            raise TypeError("Price must be a float")
        if not 1.0 <= price <= 10.0:
            raise ValueError("Price must be between 1.0 and 10.0")
        
        if not isinstance(customer, Customer):
            raise TypeError("Customer must be of type Customer")
        if not isinstance(coffee, Coffee):
            raise TypeError("Coffee must be of type Coffee")

        self.customer = customer
        self.coffee = coffee
        self._price = price
        Order.all.append(self)  

    @property
    def price(self):
        return self._price


