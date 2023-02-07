# Source: https://realpython.com/queue-in-python/#implementing-queues-in-python
# graph.py

from collections import deque
from math import inf as infinity
from typing import NamedTuple

import networkx as nx
from queue import MutableMinHeap, Queue, Stack


class City(NamedTuple):
    name: str
    country: str
    year: int | None
    latitude: float
    longitude: float
