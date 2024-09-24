# Queues - First in First out (Fifo)

from collections import deque

q = deque()

print(q)

# Enqueue - Add element to the right - O(1)
q.append(5)
q.append(6)
q.append(7)

# Deqeue (pop left) - Remove element from the left - O(1)
q.popleft()

# Peek from left side - O(1)
q[0]

# Peek from right side - O(1)
q[-1]