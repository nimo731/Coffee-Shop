from typing import List, Optional, Set
from order import Order
from coffee import Coffee

class Customer:
    """A customer in the coffee shop system."""
    
    def __init__(self, name: str) -> None:
        """Initialize a new customer with a name."""
        self._name: Optional[str] = None
        self.name = name
        self._orders: List[Order] = []

    @property
    def name(self) -> str:
        """Get the customer's name."""
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """Set the customer's name.
        
        Args:
            value (str): The new name, must be 1-15 characters.
            
        Raises:
            TypeError: If name is not a string.
            ValueError: If name length is not between 1 and 15 characters.
        """
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if not 1 <= len(value) <= 15:
            raise ValueError("Name must be between 1 and 15 characters")
        self._name = value

    def orders(self) -> List[Order]:
        """Get all orders made by this customer."""
        return self._orders

    def coffees(self) -> Set[Coffee]:
        """Get unique list of coffees ordered by this customer."""
        return set(order.coffee for order in self._orders)

    def create_order(self, coffee: Coffee, price: float) -> Order:
        """Create a new order for this customer.
        
        Args:
            coffee (Coffee): The coffee to order.
            price (float): The price of the order (1.0-10.0).
            
        Returns:
            Order: The newly created order.
        """
        order = Order(self, coffee, price)
        self._orders.append(order)
        return order

    @classmethod
    def most_aficionado(cls, coffee: Coffee) -> Optional['Customer']:
        """Find the customer who has spent the most on a particular coffee.
        
        Args:
            coffee (Coffee): The coffee to check.
            
        Returns:
            Customer or None: The customer who spent the most, or None if no orders.
        """
        if not coffee.orders():
            return None
        
        customer_spending = {}
        for order in coffee.orders():
            customer = order.customer
            if customer not in customer_spending:
                customer_spending[customer] = 0
            customer_spending[customer] += order.price
        
        return max(customer_spending.items(), key=lambda x: x[1])[0] 