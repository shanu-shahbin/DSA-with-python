import array as myarray

# Time Complexity: O(n) for creation, where n is the number of elements
# Space Complexity: O(n), where n is the number of elements

arr_int = myarray.array('i', [1,2,3,4,5])

arr_float =myarray.array('f', [1.1,2.2,3.3,4.4,5.5])

arr_str = myarray.array('u', 'Hello World')

arr_double = myarray.array('d', [1.1,2.2,3.3,4.4,5.5])

# check the typecode of the array
# Time Complexity: O(1)
# Space Complexity: O(1)
print(arr_int.typecode)
print(arr_float.typecode)
print(arr_str.typecode)
print(arr_double.typecode)

# check the length of the array
# Time Complexity: O(1)
# Space Complexity: O(1)
print(len(arr_int))

# access the elements of the array
# Time Complexity: O(1)
# Space Complexity: O(1)
print(arr_int[3])
print(arr_float[2])
print(arr_str[1])
print(arr_double[0])

# modify the elements of the array
# Time Complexity: O(1)
# Space Complexity: O(1)
arr_int[3] = 20
print(arr_int)

#add an element to the array
# Time Complexity: O(1) amortized
# Space Complexity: O(1)
arr_int.append(6)
arr_float.append(6.6)
arr_str.append('!')
arr_double.append(6.6)
print(arr_int)
print(arr_float)

#remove an element from the array
# Time Complexity: O(n), where n is the number of elements
# Space Complexity: O(1)
arr_int.remove(3)
arr_float.remove(3.299999952316284)

# insert an element to the array
# Time Complexity: O(n), where n is the number of elements after the insertion point
# Space Complexity: O(1)
arr_int.insert(3, 13)
print(arr_int)

# pop an element from the array
# Time Complexity: O(1) for popping from the end, O(n) for popping from anywhere else
# Space Complexity: O(1)
arr_int.pop()
print(arr_int)

# POP from the beginning of the array
# Time Complexity: O(n), where n is the number of elements after the popped element
# Space Complexity: O(1)
arr_int.pop(3)
print(arr_int)

# reverse the array
# Time Complexity: O(n), where n is the number of elements
# Space Complexity: O(n)

# start and end are omitted, so it considers the entire array.
#The step is -1, meaning it selects elements in reverse order.
#arr_int[:] is a way to refer to the entire array (from start to end)

arr_int_reversed = arr_int[::-1]
arr_int[:] = arr_int_reversed

arr_float_reversed = arr_float[::-1]
arr_float[:] = arr_float_reversed
