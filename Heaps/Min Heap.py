# Build Min Heap (Heapify)
# Time: O(n), Space: O(1)

A = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]

import heapq
heapq.heapify(A)

print(A)
# Heap Push (Insert element)
# Time: O(log n)

heapq.heappush(A, 4)

print(A)

# Heap Pop (Extract min)
# Time: O(log n)

minn = heapq.heappop(A)

print(A, minn)