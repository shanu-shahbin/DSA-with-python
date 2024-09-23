# Counter example to count the occurrences of characters in a string
from collections import Counter

# Input string
string = "collections module in Python provides useful tools"

# Initialize the Counter object by passing the string
# This will count the occurrences of each character in the string
counter = Counter(string)

# Display the counter (dictionary-like object showing character frequencies)
print("Character counts in the string:")
print(counter)

# Access the count of a specific character
print(f"Count of 'o': {counter['o']}")  # Output: Number of 'o' characters

# Adding more counts manually
counter.update("more characters")
print("\nAfter adding more characters:")
print(counter)

# Getting the most common elements (top 3 characters)
print("\nMost common characters (Top 3):")
print(counter.most_common(3))

# Resetting the counter
counter.clear()
print("\nAfter clearing the counter:")
print(counter)  # Output: Counter() - An empty counter
