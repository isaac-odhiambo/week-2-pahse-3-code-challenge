# test_coffee.py
import pytest

# Define the Coffee class
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


def test_coffee_creation():
    coffee = Coffee("Espresso")
    assert coffee.name == "Espresso"


def test_coffee_name_validation():
    with pytest.raises(ValueError):
        coffee = Coffee("AB")  # Less than 3 characters
    with pytest.raises(ValueError):
        coffee = Coffee(123)  # Not a string


def test_coffee_num_orders():
    coffee = Coffee("Cappuccino")
    customer = Customer("Charlie")
    coffee._orders.append(customer.create_order(coffee, 4.0))
    coffee._orders.append(customer.create_order(coffee, 6.0))
    assert coffee.num_orders() == 2


def test_coffee_average_price():
    coffee = Coffee("Americano")
    customer = Customer("David")
    coffee._orders.append(customer.create_order(coffee, 3.0))
    coffee._orders.append(customer.create_order(coffee, 5.0))
    assert coffee.average_price() == 4.0


if __name__ == "__main__":
    pytest.main()
