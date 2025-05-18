import pytest
from coffee import Coffee
from customer import Customer

def test_coffee_initialization():
    # Test valid name
    coffee = Coffee("Espresso")
    assert coffee.name == "Espresso"
    
    # Test invalid name length
    with pytest.raises(ValueError):
        Coffee("AB")  # Too short
    
    # Test invalid name type
    with pytest.raises(TypeError):
        Coffee(123)

def test_coffee_name_immutability():
    coffee = Coffee("Espresso")
    
    # Test name cannot be changed
    with pytest.raises(AttributeError):
        coffee.name = "New Name"

def test_coffee_orders():
    coffee = Coffee("Espresso")
    customer = Customer("John")
    
    # Test empty orders
    assert len(coffee.orders()) == 0
    
    # Test after creating order
    order = customer.create_order(coffee, 5.0)
    assert len(coffee.orders()) == 1
    assert order in coffee.orders()

def test_coffee_customers():
    coffee = Coffee("Espresso")
    customer1 = Customer("John")
    customer2 = Customer("Jane")
    
    # Test empty customers
    assert len(coffee.customers()) == 0
    
    # Test after creating orders
    customer1.create_order(coffee, 5.0)
    customer2.create_order(coffee, 6.0)
    
    customers = coffee.customers()
    assert len(customers) == 2
    assert customer1 in customers
    assert customer2 in customers

def test_coffee_num_orders():
    coffee = Coffee("Espresso")
    customer = Customer("John")
    
    # Test with no orders
    assert coffee.num_orders() == 0
    
    # Test with one order
    customer.create_order(coffee, 5.0)
    assert coffee.num_orders() == 1
    
    # Test with multiple orders
    customer.create_order(coffee, 6.0)
    assert coffee.num_orders() == 2

def test_coffee_average_price():
    coffee = Coffee("Espresso")
    customer = Customer("John")
    
    # Test with no orders
    assert coffee.average_price() == 0
    
    # Test with one order
    customer.create_order(coffee, 5.0)
    assert coffee.average_price() == 5.0
    
    # Test with multiple orders
    customer.create_order(coffee, 7.0)
    assert coffee.average_price() == 6.0 