class Employee:

    #To make the data members private and get them by get and set function
    def __init__(self, name, salary):
        self.name = name           # Public attribute
        self.__salary = salary      # Private attribute (Encapsulated)

    # Getter method to access the private salary attribute
    def get_salary(self):
        return self.__salary

    # Setter method to modify the private salary attribute
    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Salary must be positive!")

# Create an object of the Employee class
emp = Employee("John", 5000)

# Access the public attribute
print(f"Employee Name: {emp.name}")  # Output: Employee Name: John

# Access the private attribute using the getter method
print(f"Initial Salary: {emp.get_salary()}")  # Output: Initial Salary: 5000

# Modify the private attribute using the setter method
emp.set_salary(6000)
print(f"Updated Salary: {emp.get_salary()}")  # Output: Updated Salary: 6000

# Attempt to set an invalid salary
emp.set_salary(-100)  # Output: Salary must be positive!
