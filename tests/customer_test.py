import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_customer_initialization():
    # Test valid name
    customer = Customer("John")
    assert customer.name == "John"
    
    # Test invalid name length
    with pytest.raises(ValueError):
        Customer("")  # Too short
    
    with pytest.raises(ValueError):
        Customer("A" * 16)  # Too long
    
    # Test invalid name type
    with pytest.raises(TypeError):
        Customer(123)

def test_customer_name_property():
    customer = Customer("John")
    
    # Test valid name change
    customer.name = "Jane"
    assert customer.name == "Jane"
    
    # Test invalid name change
    with pytest.raises(ValueError):
        customer.name = "A" * 16
    
    with pytest.raises(TypeError):
        customer.name = 123

def test_customer_orders():
    customer = Customer("John")
    coffee = Coffee("Espresso")
    
    # Test empty orders
    assert len(customer.orders()) == 0
    
    # Test after creating order
    order = customer.create_order(coffee, 5.0)
    assert len(customer.orders()) == 1
    assert order in customer.orders()

def test_customer_coffees():
    customer = Customer("John")
    coffee1 = Coffee("Espresso")
    coffee2 = Coffee("Latte")
    
    # Test empty coffees
    assert len(customer.coffees()) == 0
    
    # Test after creating orders
    customer.create_order(coffee1, 5.0)
    customer.create_order(coffee2, 6.0)
    
    coffees = customer.coffees()
    assert len(coffees) == 2
    assert coffee1 in coffees
    assert coffee2 in coffees

def test_most_aficionado():
    coffee = Coffee("Espresso")
    customer1 = Customer("John")
    customer2 = Customer("Jane")
    
    # Test with no orders
    assert Customer.most_aficionado(coffee) is None
    
    # Test with single customer
    customer1.create_order(coffee, 5.0)
    assert Customer.most_aficionado(coffee) == customer1
    
    # Test with multiple customers
    customer2.create_order(coffee, 6.0)
    assert Customer.most_aficionado(coffee) == customer2
    
    # Test with equal spending
    customer1.create_order(coffee, 6.0)
    assert Customer.most_aficionado(coffee) in [customer1, customer2] 