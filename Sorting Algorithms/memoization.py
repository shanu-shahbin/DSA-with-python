# memoization or top-down approach

def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]

# Sample input
n = 10
result = fibonacci(n)
print(f"The {n}th Fibonacci number is: {result}")