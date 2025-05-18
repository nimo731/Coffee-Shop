from typing import List, Set
from customer import Customer
from order import Order
from constants import (
    MIN_COFFEE_NAME_LENGTH,
    ERROR_MESSAGES
)

class Coffee:
    """A coffee product in the coffee shop system."""
    
    def __init__(self, name: str) -> None:
        """Initialize a new coffee with a name.
        
        Args:
            name (str): The name of the coffee, must be at least 3 characters.
            
        Raises:
            TypeError: If name is not a string.
            ValueError: If name is less than 3 characters.
        """
        self._name: str = None
        self.name = name
        self._orders: List[Order] = []

    @property
    def name(self) -> str:
        """Get the coffee's name."""
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """Set the coffee's name.
        
        Args:
            value (str): The new name, must be at least 3 characters.
            
        Raises:
            TypeError: If name is not a string.
            ValueError: If name is less than 3 characters.
            AttributeError: If trying to change name after initialization.
        """
        if not isinstance(value, str):
            raise TypeError(ERROR_MESSAGES['coffee_name_type'])
        if len(value) < MIN_COFFEE_NAME_LENGTH:
            raise ValueError(ERROR_MESSAGES['coffee_name_length'])
        if self._name is not None:
            raise AttributeError(ERROR_MESSAGES['coffee_name_immutable'])
        self._name = value

    def orders(self) -> List[Order]:
        """Get all orders for this coffee."""
        return self._orders

    def customers(self) -> Set[Customer]:
        """Get unique list of customers who have ordered this coffee."""
        return set(order.customer for order in self._orders)

    def num_orders(self) -> int:
        """Get the total number of orders for this coffee."""
        return len(self._orders)

    def average_price(self) -> float:
        """Calculate the average price of all orders for this coffee.
        
        Returns:
            float: The average price, or 0 if no orders exist.
        """
        if not self._orders:
            return 0
        return sum(order.price for order in self._orders) / len(self._orders) 