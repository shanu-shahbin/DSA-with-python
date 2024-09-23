from collections import defaultdict

# Initialize defaultdict with a default factory of list
# defaultdict will automatically assign an empty list to any key that does not exist yet
default = defaultdict(list)

# Accessing a non-existing key automatically creates a new key with an empty list as the value
print(default[2])  # Output: []

# Adding elements to the list corresponding to key 2
default[2].append(10)
default[2].append(20)
print(f"After adding elements to key 2: {default[2]}")  # Output: [10, 20]

# Accessing another non-existing key automatically creates a new key with an empty list
print(default[5])  # Output: []

# Adding elements to the list corresponding to key 5
default[5].append(50)
print(f"After adding an element to key 5: {default[5]}")  # Output: [50]

# Adding another element to key 5
default[5].append(100)
print(f"After adding more elements to key 5: {default[5]}")  # Output: [50, 100]

# You can also manually assign values to new keys
default[1] = [1, 2, 3]
print(f"Key 1 has the value: {default[1]}")  # Output: [1, 2, 3]

# Printing the entire defaultdict
print("Full defaultdict content:")
for key, value in default.items():
    print(f"Key {key}: {value}")

# Output of full defaultdict:
# Key 2: [10, 20]
# Key 5: [50, 100]
# Key 1: [1, 2, 3]
