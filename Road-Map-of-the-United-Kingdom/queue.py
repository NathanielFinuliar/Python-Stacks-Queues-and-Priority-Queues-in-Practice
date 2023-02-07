# Source: https://realpython.com/queue-in-python/#implementing-queues-in-python
# queues.py

from collections import deque
from dataclasses import dataclass
from heapq import heapify, heappop, heappush
from itertools import count
from typing import Any

