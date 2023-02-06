# Queue class Code Source: https://realpython.com/queue-in-python/#implementing-queues-in-python
from collections import deque
from heapq import heappop, heappush

class Queue:
    def __init__(self, *elements):
        self._elements = deque(elements)
