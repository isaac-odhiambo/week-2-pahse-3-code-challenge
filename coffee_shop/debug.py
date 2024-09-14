from customer import Customer
from coffee import Coffee

customer = Customer("John")
coffee = Coffee("Latte")

order = customer.create_order(coffee, 5.0)

print(f"Customer: {customer.name}")
print(f"Coffee: {coffee.name}")
print(f"Order Price: {order.price}")

print(f"Customer's Orders: {[o.coffee.name for o in customer.orders()]}")
print(f"Coffee's Orders: {coffee.num_orders()}")
print(f"Average price of {coffee.name}: {coffee.average_price()}")
