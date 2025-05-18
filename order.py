class Order:
    def __init__(self, customer, coffee, price):
        self._customer = None
        self._coffee = None
        self._price = None
        
        self.customer = customer
        self.coffee = coffee
        self.price = price

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):
        if not isinstance(value, type(self._customer)) and self._customer is not None:
            raise TypeError("Customer must be a Customer instance")
        self._customer = value

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, value):
        if not isinstance(value, type(self._coffee)) and self._coffee is not None:
            raise TypeError("Coffee must be a Coffee instance")
        self._coffee = value
        if value is not None:
            value._orders.append(self)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, float):
            raise TypeError("Price must be a float")
        if not 1.0 <= value <= 10.0:
            raise ValueError("Price must be between 1.0 and 10.0")
        if self._price is not None:
            raise AttributeError("Order price cannot be changed after initialization")
        self._price = value 