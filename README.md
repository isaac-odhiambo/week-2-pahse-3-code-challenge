# week-2-pahse-3-code-challenge
# Coffee Shop Domain Modeling
# Objective
Design and implement a Python application to model a Coffee Shop domain using object-oriented programming principles. This assessment will evaluate your ability to design classes, establish relationships between objects, implement methods, and handle data validation and exceptions.


Identify the three main classes: Customer, Coffee, and Order.
Establish the relationships between these classes.
Determine the attributes and methods that each class will have.
Considered  the concept of a single source of truth for your data.

# Implement Initializers and Properties
Customer Class (customer.py):

Initialize a Customer with a name (string between 1 and 15 characters).
Implement a property name with the necessary validation.
Coffee Class (coffee.py):

Initialize a Coffee with a name (string, at least 3 characters long).
Implement a property name with the necessary validation.
Order Class (order.py):

Initialize an Order with a Customer instance, a Coffee instance, and a price (float between 1.0 and 10.0).
Implement properties customer, coffee, and price with the necessary validation.

# Define Object Relationship Methods and Properties
Order Class (order.py):

customer property returns the Customer instance for the order.
coffee property returns the Coffee instance for the order.
Coffee Class (coffee.py):

orders() method returns a list of all Order instances for that coffee.
customers() method returns a unique list of Customer instances who have ordered that coffee.
Customer Class (customer.py):

orders() method returns a list of all Order instances for that customer.
coffees() method returns a unique list of Coffee instances that the customer has ordered.



# Customer:
Attributes: name
Methods: name getter and setter with validation
# Coffee:
Attributes: name
Methods: name getter and setter with validation
# Order:
Attributes: customer (instance of Customer), coffee (instance of Coffee), price
Methods: customer, coffee, and price getters and setters with validation
# Relationships:

A Customer can place multiple Orders.
An Order is associated with one Customer and one Coffee.
A Coffee can appear in multiple Orders.



#  Points To Note:
# Initialization Tests: 
Each test file includes tests for validating correct initialization of attributes.
Validation Tests: Tests check for valid and invalid inputs to ensure attributes are set correctly and exceptions are raised appropriately.

# Test Execution: 
The if __name__ == "__main__": block is included to allow running the tests directly from the test file.
This setup ensures that your tests are separated into different files and verifies the correct functionality of your classes while avoiding import issues.