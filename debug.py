from customer import Customer
from coffee import Coffee
from order import Order

# Create instances
customer = Customer("John")
coffee = Coffee("Espresso")

# Test customer name validation
try:
    customer.name = "A" * 16  # Should raise ValueError
except ValueError as e:
    print(f"Expected error: {e}")

try:
    customer.name = 123  # Should raise TypeError
except TypeError as e:
    print(f"Expected error: {e}")

# Test coffee name validation
try:
    coffee.name = "AB"  # Should raise ValueError
except ValueError as e:
    print(f"Expected error: {e}")

try:
    coffee.name = "New Name"  # Should raise AttributeError
except AttributeError as e:
    print(f"Expected error: {e}")

# Create an order
order = customer.create_order(coffee, 5.0)

# Test relationships
print(f"Customer orders: {len(customer.orders())}")  # Should be 1
print(f"Customer coffees: {len(customer.coffees())}")  # Should be 1
print(f"Coffee orders: {len(coffee.orders())}")  # Should be 1
print(f"Coffee customers: {len(coffee.customers())}")  # Should be 1

# Test aggregates
print(f"Number of orders for coffee: {coffee.num_orders()}")  # Should be 1
print(f"Average price: {coffee.average_price()}")  # Should be 5.0

# Test most_aficionado
most_spender = Customer.most_aficionado(coffee)
print(f"Most aficionado: {most_spender.name if most_spender else 'None'}")  # Should be "John" 