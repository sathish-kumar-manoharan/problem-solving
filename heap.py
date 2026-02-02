import heapq
from dataclasses import dataclass, field

@dataclass(order=True)
class Node:   
    key: int = field(compare=False)
    value: int = field(compare=True)


    def __init__(self, key, value):
        self.key = key
        self.value = value

max_heap = []

for index in range(10):
    node = Node(index, (index+100))
    heapq.heappush(max_heap, node)


while max_heap:
    node = heapq.heappop(max_heap)
    print(f"The key is {node.key} and value is {node.value}")