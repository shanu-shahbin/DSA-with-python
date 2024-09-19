
arr_int = [1,2,3,4,5,6,7,8,9]
print(arr_int)

# Append - Insert element at end of array - On average: O(1)
arr_int.append(10)
print(arr_int)

# Pop - Deleting element at end of array - O(1)
arr_int.pop()
print(arr_int)

#insert (not at end of array) - O(n)
arr_int.insert(1,10)
print(arr_int)

# Modify an element - O(1)
arr_int[1] = 100
print(arr_int)

# Accessing element given index i - O(1)
print(arr_int[2])

# Checking length - O(1)
print(len(arr_int))

arr_str = ["a","b","c","d","e"]
print(arr_str)
arr_str2 = ["shane"]
print(arr_str2)

#concatenate
arr_str3 = arr_str + arr_str2
print(arr_str3)

# Append to end of string - O(n)
arr_str = arr_str + ["watson"]
print(arr_str)

# Check if something is in string - O(n)
if "watson" in arr_str:
    print("Found")
else:
    print("Not Found")

# Iterating through array - O(n)
for i in arr_str:
    print(i)

# reverse array - O(n)

arr_str.reverse()
print("Reversed string array:", arr_str)


# reverse without using built in function - O(n)
# Time Complexity: O(n) - We swap elements from both ends of the array towards the center.
# Space Complexity: O(1) - No extra space is used except for a few variables.

arr_original = [1,2,3,4,5,6,7,8,9]
n = len(arr_original)
for i in range( n //2 ):
    # Swap the elements at indices i and n-i-1 
    arr_original[i], arr_original[n-i-1] = arr_original[n-i-1], arr_original[i]
print(arr_original)

# n is the length of the array.
# i is the current index from the left side during the iteration.
# n-i-1 calculates the corresponding index from the right side of the array, which mirrors the index i from the left.  
# For i = 2, n-i-1 = 9-2-1 = 6. So arr_int[n-i-1] refers to arr_int[6] (which is 7).