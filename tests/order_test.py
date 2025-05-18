import pytest
from order import Order
from customer import Customer
from coffee import Coffee

def test_order_initialization():
    customer = Customer("John")
    coffee = Coffee("Espresso")
    
    # Test valid order
    order = Order(customer, coffee, 5.0)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 5.0
    
    # Test invalid price type
    with pytest.raises(TypeError):
        Order(customer, coffee, "5.0")
    
    # Test invalid price range
    with pytest.raises(ValueError):
        Order(customer, coffee, 0.5)  # Too low
    
    with pytest.raises(ValueError):
        Order(customer, coffee, 11.0)  # Too high

def test_order_price_immutability():
    customer = Customer("John")
    coffee = Coffee("Espresso")
    order = Order(customer, coffee, 5.0)
    
    # Test price cannot be changed
    with pytest.raises(AttributeError):
        order.price = 6.0

def test_order_relationships():
    customer = Customer("John")
    coffee = Coffee("Espresso")
    order = Order(customer, coffee, 5.0)
    
    # Test customer relationship
    assert order.customer == customer
    assert order in customer.orders()
    
    # Test coffee relationship
    assert order.coffee == coffee
    assert order in coffee.orders()

def test_order_type_checking():
    customer = Customer("John")
    coffee = Coffee("Espresso")
    order = Order(customer, coffee, 5.0)
    
    # Test invalid customer type
    with pytest.raises(TypeError):
        order.customer = "Invalid"
    
    # Test invalid coffee type
    with pytest.raises(TypeError):
        order.coffee = "Invalid" 