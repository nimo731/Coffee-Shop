"""Constants used throughout the coffee shop system."""

# Name validation
MIN_CUSTOMER_NAME_LENGTH = 1
MAX_CUSTOMER_NAME_LENGTH = 15
MIN_COFFEE_NAME_LENGTH = 3

# Price validation
MIN_ORDER_PRICE = 1.0
MAX_ORDER_PRICE = 10.0

# Error messages
ERROR_MESSAGES = {
    'customer_name_type': "Name must be a string",
    'customer_name_length': f"Name must be between {MIN_CUSTOMER_NAME_LENGTH} and {MAX_CUSTOMER_NAME_LENGTH} characters",
    'coffee_name_type': "Name must be a string",
    'coffee_name_length': f"Name must be at least {MIN_COFFEE_NAME_LENGTH} characters long",
    'coffee_name_immutable': "Coffee name cannot be changed after initialization",
    'order_price_type': "Price must be a float",
    'order_price_range': f"Price must be between {MIN_ORDER_PRICE} and {MAX_ORDER_PRICE}",
    'order_price_immutable': "Order price cannot be changed after initialization",
    'customer_type': "Customer must be a Customer instance",
    'coffee_type': "Coffee must be a Coffee instance"
} 