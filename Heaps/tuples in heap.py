# Putting tuples of items on the heap
import heapq

D = [5, 4, 3, 5, 4, 3, 5, 5, 4]

from collections import Counter

counter = Counter(D)

print(counter)

heap = []

for k, v in counter.items():
  heapq.heappush(heap, (v, k))

print(heap)