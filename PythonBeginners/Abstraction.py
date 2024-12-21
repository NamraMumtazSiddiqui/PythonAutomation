from abc import ABC, abstractmethod
#Abstraction allows you to define methods that must be implemented in derived classes without
# providing the implementation details in the base class. This is useful for creating a common
# interface for a group of related classes.

# Abstract base class
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        """Method that must be implemented in derived classes"""
        pass

    @abstractmethod
    def stop_engine(self):
        """Method that must be implemented in derived classes"""
        pass

# Concrete class 1
class Car(Vehicle):
    def start_engine(self):
        return "Car engine started."

    def stop_engine(self):
        return "Car engine stopped."

# Concrete class 2
class Motorcycle(Vehicle):
    def start_engine(self):
        return "Motorcycle engine started."

    def stop_engine(self):
        return "Motorcycle engine stopped."

# Creating instances of concrete classes
car = Car()
motorcycle = Motorcycle()

# Using the abstraction
print(car.start_engine())     # Output: Car engine started.
print(car.stop_engine())      # Output: Car engine stopped.
print(motorcycle.start_engine())  # Output: Motorcycle engine started.
print(motorcycle.stop_engine())   # Output: Motorcycle engine stopped.
# # Assign the value of the 'name' parameter to the instance attribute 'name'
#A constructor is a special method within a class that is automatically called when an object
# (instance) of that class is created.class Person:

#     def __init__(self, name, age):  # Constructor
#         self.name = name
#         self.age = age
# In this example, __init__ is the constructor method that initializes the name and age attributes of the Person class.
#self is a reference to the current instance of the class. It allows you to access the
#instance's attributes and methods from within the class.


