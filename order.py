class Order:
    """An order linking a customer to a coffee with a specific price."""
    
    def __init__(self, customer, coffee, price):
        """Initialize a new order.
        
        Args:
            customer (Customer): The customer making the order.
            coffee (Coffee): The coffee being ordered.
            price (float): The price of the order (1.0-10.0).
            
        Raises:
            TypeError: If price is not a float.
            ValueError: If price is not between 1.0 and 10.0.
        """
        self._customer = None
        self._coffee = None
        self._price = None
        
        self.customer = customer
        self.coffee = coffee
        self.price = price

    @property
    def customer(self):
        """Get the customer who made this order."""
        return self._customer

    @customer.setter
    def customer(self, value):
        """Set the customer for this order.
        
        Args:
            value (Customer): The customer making the order.
            
        Raises:
            TypeError: If value is not a Customer instance.
        """
        if not isinstance(value, type(self._customer)) and self._customer is not None:
            raise TypeError("Customer must be a Customer instance")
        self._customer = value

    @property
    def coffee(self):
        """Get the coffee in this order."""
        return self._coffee

    @coffee.setter
    def coffee(self, value):
        """Set the coffee for this order.
        
        Args:
            value (Coffee): The coffee being ordered.
            
        Raises:
            TypeError: If value is not a Coffee instance.
        """
        if not isinstance(value, type(self._coffee)) and self._coffee is not None:
            raise TypeError("Coffee must be a Coffee instance")
        self._coffee = value
        if value is not None:
            value._orders.append(self)

    @property
    def price(self):
        """Get the price of this order."""
        return self._price

    @price.setter
    def price(self, value):
        """Set the price of this order.
        
        Args:
            value (float): The price (1.0-10.0).
            
        Raises:
            TypeError: If price is not a float.
            ValueError: If price is not between 1.0 and 10.0.
            AttributeError: If trying to change price after initialization.
        """
        if not isinstance(value, float):
            raise TypeError("Price must be a float")
        if not 1.0 <= value <= 10.0:
            raise ValueError("Price must be between 1.0 and 10.0")
        if self._price is not None:
            raise AttributeError("Order price cannot be changed after initialization")
        self._price = value 