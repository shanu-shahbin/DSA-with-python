
# Fibonacci
# 0,  1, 1, 2, 3, 5, 8, 13, 21, 34, 55
# f(0) = 0
# f(1) = 1
# n > 1: F(n) = F(n-1) + F(n-2)

# Time: O(2^n), Space: O(n)

def F(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return F(n-1) + F(n-2)

print(F(12))