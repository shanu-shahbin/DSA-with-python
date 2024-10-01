
# Max Heap
import heapq

B = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]
n = len(B)

for i in range(n):
  B[i] = -B[i]

heapq.heapify(B)

largest = -heapq.heappop(B)
print(largest)

heapq.heappush(B, -7) # Insert 7 into max heap
print(B)