class SimpleClass:
    def __init__(self, value):
        self.value = value
    def display_value(self):
        print("The value is:", self.value)

    def add_number(a,b):
        return a+b

    result=add_number(5,6)
    print("The Sum is ",result)

# Create an object of SimpleClass
obj = SimpleClass(10)

# Call the display_value method
obj.display_value()



#Ascending order
numbers=[5,3,4,8,9]
sorted_numbers=sorted(numbers)
print("Sorted List", sorted_numbers)

#Descending Order

number=[5,3,4,8,9]
reverse_numbers = sorted(number, reverse=True)
print("Sorted List", reverse_numbers)

#Sorting Manually by using Bubble Sort

# Initialize the list of numbers
numbers = [5, 3, 8, 6, 2]

# Get the length of the list
n = len(numbers)
425
# Bubble Sort Algorithm
for i in range(n):
    for j in range(0, n - i - 1):
        if numbers[j] > numbers[j + 1]:
            # Swap if the element found is greater than the next element
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

# Print the sorted list
print("Sorted list:", numbers)

#Descending order
# Initialize the list of numbers
numbers = [5, 3, 8, 6, 2]

# Bubble Sort Algorithm for descending order
n = len(numbers)
for i in range(n):
    for j in range(0, n - i - 1):
        if numbers[j] < numbers[j + 1]:
            # Swap if the element found is smaller than the next element
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

# Print the sorted list
print("Sorted list in descending order:", numbers)
