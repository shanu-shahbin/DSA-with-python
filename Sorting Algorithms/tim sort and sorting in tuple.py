# Sort array of tuples

I = [(-5, 3), (2, 1), (-3, -3), (7, 2), (2, 2)]

sorted_I = sorted(I, key = lambda t: -t[1])

print(sorted_I)

# for positive numbers
I = [(-5, 3), (2, 1), (-3, -3), (7, 2), (2, 2)]

sorted_I = sorted(I, key = lambda t: t[1])

print(sorted_I)


# Time complexity is O(n log n) from using Tim Sort

G = [-5, 3, 2, 1, -3, -3, 7, 2, 2]

# In place (constant space)
G.sort()

print(G)

# Get new sorted array - O(n) space

H = [-5, 3, 2, 1, -3, -3, 7, 2, 2]

sorted_H = sorted(H)

print(H, sorted_H)