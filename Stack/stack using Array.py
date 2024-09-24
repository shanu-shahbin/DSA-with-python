# Stacks - Last in First Out (Lifo)

stack = []
print(stack)

# Append to top of stack - O(1)
stack.append(5)
stack.append(4)
stack.append(3)

# Pop from stack - O(1)
x = stack.pop()

print(x)
print(stack)

# Ask what's on the top of stack - O(1)
print(stack[-1])

# Ask if something is in the stack - O(1)
if stack:
  print(True)