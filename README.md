# Coffee Shop Challenge

A Python implementation of a coffee shop domain model with relationships between Customers, Coffees, and Orders.

## Project Structure

```
coffee-shop-challenge/
├── Pipfile
├── debug.py
├── customer.py
├── coffee.py
├── order.py
└── tests/
    ├── customer_test.py
    ├── coffee_test.py
    └── order_test.py
```

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd coffee-shop-challenge
```

2. Install dependencies:
```bash
pipenv install
pipenv shell
```

## Models

### Customer
- Has a name (1-15 characters)
- Can place orders
- Can view their order history
- Can view unique coffees they've ordered

### Coffee
- Has a name (minimum 3 characters)
- Tracks all orders
- Can calculate average price and number of orders
- Can list all customers who have ordered it

### Order
- Links a Customer to a Coffee
- Has a price (1.0-10.0)
- Price is immutable after creation

## Usage

Run the debug file to see example usage:
```bash
python debug.py
```

## Testing

Run tests using pytest:
```bash
pytest
``` 