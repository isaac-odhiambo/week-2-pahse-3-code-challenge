# test_customer.py
import pytest

# Define the Customer class
class Customer:
    def __init__(self, name):
        self.name = name
        self._orders = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise ValueError("Invalid name")

    @property
    def orders(self):
        return self._orders

    def create_order(self, coffee, price):
        return Order(self, coffee, price)


class Order:
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price


class Coffee:
    def __init__(self, name):
        self.name = name
        self._orders = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) >= 3:
            self._name = value
        else:
            raise ValueError("Invalid name")

    @property
    def orders(self):
        return self._orders

    def num_orders(self):
        return len(self._orders)

    def average_price(self):
        if not self._orders:
            return 0
        total_price = sum(order.price for order in self._orders)
        return total_price / len(self._orders)


def test_customer_creation():
    c = Customer("Alice")
    assert c.name == "Alice"


def test_customer_name_validation():
    with pytest.raises(ValueError):
        c = Customer("ThisNameIsWayTooLong")  # Exceeds 15 characters
    with pytest.raises(ValueError):
        c = Customer("")  # Less than 1 character


def test_create_order():
    customer = Customer("Bob")
    coffee = Coffee("Latte")
    order = customer.create_order(coffee, 5.0)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 5.0


if __name__ == "__main__":
    pytest.main()
