 import numpy as np

array1 = [1, 2, 3]
array2 = [4, 5, 6]

sum_array = np.add(array1, array2)
print("Sum of Arrays", sum_array)

# By User Input

def user_input():
    size = int(input("Enter size of an array"))
    print("Enter elements of first array")
    arr1 = np.array([int(x) for x in input().split()])

    print("Enter elements of second array")
    arr2 = np.array([int(x) for x in input().split()])

    if len(arr1) != size or len(arr2) != size:
        print("Array Size Mismatched")
        return


    sumofarray = np.add(arr1 ,arr2)
    print("Sum of arrays", sumofarray)

user_input()
