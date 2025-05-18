from customer import Customer
from coffee import Coffee
from order import Order

def test_customer_validation():
    print("\nTesting Customer Validation:")
    try:
        customer = Customer("John")
        print("✓ Valid customer name created")
    except Exception as e:
        print(f"✗ Error creating valid customer: {e}")

    try:
        customer.name = "A" * 16  # Should raise ValueError
        print("✗ Should have raised ValueError for long name")
    except ValueError as e:
        print(f"✓ Caught ValueError for long name: {e}")

    try:
        customer.name = 123  # Should raise TypeError
        print("✗ Should have raised TypeError for non-string name")
    except TypeError as e:
        print(f"✓ Caught TypeError for non-string name: {e}")

def test_coffee_validation():
    print("\nTesting Coffee Validation:")
    try:
        coffee = Coffee("Espresso")
        print("✓ Valid coffee name created")
    except Exception as e:
        print(f"✗ Error creating valid coffee: {e}")

    try:
        coffee.name = "AB"  # Should raise ValueError
        print("✗ Should have raised ValueError for short name")
    except ValueError as e:
        print(f"✓ Caught ValueError for short name: {e}")

    try:
        coffee.name = "New Name"  # Should raise AttributeError
        print("✗ Should have raised AttributeError for changing name")
    except AttributeError as e:
        print(f"✓ Caught AttributeError for changing name: {e}")

def test_order_validation():
    print("\nTesting Order Validation:")
    customer = Customer("John")
    coffee = Coffee("Espresso")
    
    try:
        order = Order(customer, coffee, 5.0)
        print("✓ Valid order created")
    except Exception as e:
        print(f"✗ Error creating valid order: {e}")

    try:
        Order(customer, coffee, 0.5)  # Should raise ValueError
        print("✗ Should have raised ValueError for low price")
    except ValueError as e:
        print(f"✓ Caught ValueError for low price: {e}")

    try:
        Order(customer, coffee, 11.0)  # Should raise ValueError
        print("✗ Should have raised ValueError for high price")
    except ValueError as e:
        print(f"✓ Caught ValueError for high price: {e}")

def test_relationships():
    print("\nTesting Relationships:")
    customer = Customer("John")
    coffee = Coffee("Espresso")
    
    # Create orders
    order1 = customer.create_order(coffee, 5.0)
    order2 = customer.create_order(coffee, 6.0)
    
    # Test customer orders
    print(f"Customer orders: {len(customer.orders())}")  # Should be 2
    print(f"Customer coffees: {len(customer.coffees())}")  # Should be 1
    
    # Test coffee orders
    print(f"Coffee orders: {len(coffee.orders())}")  # Should be 2
    print(f"Coffee customers: {len(coffee.customers())}")  # Should be 1
    
    # Test aggregates
    print(f"Number of orders for coffee: {coffee.num_orders()}")  # Should be 2
    print(f"Average price: {coffee.average_price()}")  # Should be 5.5

def test_most_aficionado():
    print("\nTesting Most Aficionado:")
    coffee = Coffee("Espresso")
    customer1 = Customer("John")
    customer2 = Customer("Jane")
    
    # Test with no orders
    assert Customer.most_aficionado(coffee) is None
    print("✓ Returns None when no orders exist")
    
    # Test with single customer
    customer1.create_order(coffee, 5.0)
    assert Customer.most_aficionado(coffee) == customer1
    print("✓ Correctly identifies single customer")
    
    # Test with multiple customers
    customer2.create_order(coffee, 6.0)
    assert Customer.most_aficionado(coffee) == customer2
    print("✓ Correctly identifies highest spender")
    
    # Test with equal spending
    customer1.create_order(coffee, 6.0)
    result = Customer.most_aficionado(coffee)
    assert result in [customer1, customer2]
    print(f"✓ Correctly handles equal spending: {result.name}")

if __name__ == "__main__":
    print("Running Coffee Shop Tests...")
    test_customer_validation()
    test_coffee_validation()
    test_order_validation()
    test_relationships()
    test_most_aficionado()
    print("\nAll tests completed!") 