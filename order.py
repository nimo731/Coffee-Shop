from typing import Optional
from customer import Customer
from coffee import Coffee
from constants import (
    MIN_ORDER_PRICE,
    MAX_ORDER_PRICE,
    ERROR_MESSAGES
)

class Order:
    """An order linking a customer to a coffee with a specific price."""
    
    def __init__(self, customer: Customer, coffee: Coffee, price: float) -> None:
        """Initialize a new order.
        
        Args:
            customer (Customer): The customer making the order.
            coffee (Coffee): The coffee being ordered.
            price (float): The price of the order (1.0-10.0).
            
        Raises:
            TypeError: If price is not a float.
            ValueError: If price is not between 1.0 and 10.0.
        """
        self._customer: Optional[Customer] = None
        self._coffee: Optional[Coffee] = None
        self._price: Optional[float] = None
        
        self.customer = customer
        self.coffee = coffee
        self.price = price

    @property
    def customer(self) -> Customer:
        """Get the customer who made this order."""
        return self._customer

    @customer.setter
    def customer(self, value: Customer) -> None:
        """Set the customer for this order.
        
        Args:
            value (Customer): The customer making the order.
            
        Raises:
            TypeError: If value is not a Customer instance.
        """
        if not isinstance(value, type(self._customer)) and self._customer is not None:
            raise TypeError(ERROR_MESSAGES['customer_type'])
        self._customer = value

    @property
    def coffee(self) -> Coffee:
        """Get the coffee in this order."""
        return self._coffee

    @coffee.setter
    def coffee(self, value: Coffee) -> None:
        """Set the coffee for this order.
        
        Args:
            value (Coffee): The coffee being ordered.
            
        Raises:
            TypeError: If value is not a Coffee instance.
        """
        if not isinstance(value, type(self._coffee)) and self._coffee is not None:
            raise TypeError(ERROR_MESSAGES['coffee_type'])
        self._coffee = value
        if value is not None:
            value._orders.append(self)

    @property
    def price(self) -> float:
        """Get the price of this order."""
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        """Set the price of this order.
        
        Args:
            value (float): The price (1.0-10.0).
            
        Raises:
            TypeError: If price is not a float.
            ValueError: If price is not between 1.0 and 10.0.
            AttributeError: If trying to change price after initialization.
        """
        if not isinstance(value, float):
            raise TypeError(ERROR_MESSAGES['order_price_type'])
        if not MIN_ORDER_PRICE <= value <= MAX_ORDER_PRICE:
            raise ValueError(ERROR_MESSAGES['order_price_range'])
        if self._price is not None:
            raise AttributeError(ERROR_MESSAGES['order_price_immutable'])
        self._price = value 