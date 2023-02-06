# Queue class Code Source: https://realpython.com/queue-in-python/#implementing-queues-in-python
from collections import deque
from heapq import heappop, heappush

class Queue:
    def __init__(self, *elements):
        self._elements = deque(elements)

    def __len__(self):
        return len(self._elements)

    def __iter__(self):
        while len(self) > 0:
            yield self.dequeue()

    def enqueue(self, element):
        self._elements.append(element)
