"""
https://leetcode.com/problems/shortest-path-in-a-hidden-grid
"""
# """
# This is GridMaster's API interface.
# You should not implement it, or speculate about its implementation
# """
from collections import deque

class GridMaster(object):
   def canMove(self, direction: str) -> bool:
       return True

   def move(self, direction: str) -> bool:
       return True

   def isTarget(self) -> None:
    return True

class Solution(object):
    def findShortestPath(self, master: 'GridMaster') -> int:
        if not master:
            return -1

        is_target_found = False

        lookup = {'L': [0, -1], 'R': [0, 1], 'U': [-1, 0], 'D': [1, 0]}
        opposites = {'L': 'R', 'R': 'L', 'U' : 'D', 'D': 'U'}
        graph = {}
       
        def build_graph(row, col):
            graph[(row, col)] = master.isTarget()

            for dir in {'L', 'R', 'U', 'D'}:
                if master.canMove(dir):
                    dx, dy = lookup[dir]
                    next_row, next_col = row + dx , col + dy

                    if (next_row, next_col) not in graph:
                        master.move(dir)
                        build_graph(next_row, next_col)
                        master.move(opposites[dir])

        build_graph(0,0)

        queue = deque([(0, 0, 0)])
        visited = set([0, 0])

        while queue:
            row, col, steps = queue.popleft()

            if graph[(row, col)]:
                return steps

            for r, c in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                next_row = row + r
                next_col = col + c

                if (next_row, next_col) in graph and (next_row, next_col) not in visited:
                    visited.add((next_row, next_col))
                    queue.append((next_row, next_col, steps + 1))

        return -1

