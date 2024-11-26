"""
https://leetcode.com/problems/clone-graph
"""

from collections import deque
from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def __init__(self):
        self.visited = {}

    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:

        if not node:
            return node

        visited = {}
        queue = deque([node])
        visited[node] = Node(node.val, [])

        while queue:
            current = queue.popleft()

            for neighbor in current.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val, [])
                    queue.append(neighbor)
                visited[current].neighbors.append(visited[neighbor])

        return visited[node]


    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        if node in self.visited:
            return self.visited[node]

        clone_node = Node(node.val, [])

        self.visited[node] = clone_node

        if node.neighbors:
            clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]

        return clone_node