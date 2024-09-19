import numpy as np

# Creating an integer array
arr_int = np.array([1, 2, 3, 4, 5])
print("Original array:", arr_int)

# Append element to the array
# Time Complexity: O(n) - A new array is created with size n+1, copying elements.
# Space Complexity: O(n) - A new array of size n+1 is created.
arr_int = np.append(arr_int, [6])
print("After append:", arr_int)

# Insert an element at a specific position (e.g., insert 10 at index 2)
# Time Complexity: O(n) - Elements after the index need to be shifted.
# Space Complexity: O(n) - A new array of size n+1 is created.
arr_int = np.insert(arr_int, 2, 10)
print("After insert:", arr_int)

# Reverse the array
# Time Complexity: O(n) - All elements need to be traversed to reverse.
# Space Complexity: O(n) - A new array of the same size is created in reversed order.
arr_reversed = np.flip(arr_int)
print("Reversed array:", arr_reversed)

# Pop the last element (NumPy doesn't have a built-in pop, so we slice the array)
# Time Complexity: O(n) - A new array is created without the last element.
# Space Complexity: O(n) - A new array of size n-1 is created.
arr_int = arr_int[:-1]
print("After pop:", arr_int)

# Additional examples: Array with float elements
arr_float = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
print("Float array:", arr_float)

# 2D array example
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D array:", arr_2d)

# 3D array example
arr_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print("3D array:", arr_3d)
