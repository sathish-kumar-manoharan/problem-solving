from collections import deque
from typing import List

"""
https://leetcode.com/problems/number-of-closed-islands/submissions/

"""

class Solution:


    def closedIsland(self, grid: List[List[int]]) -> int:
        count = 0
        
        if not grid:
            return count
        
        rows = len(grid)
        cols = len(grid[0])
        
        
        def dfs(row, col):
            if 0 > row or row >= rows or 0 > col or col >= cols:
                return False
            
            if grid[row][col] == 1:
                return True
            
            grid[row][col] = 1
            
            left = dfs(row, col-1)
            right = dfs(row, col+1)
            up = dfs(row-1, col)
            down = dfs(row+1, col)
            
            return left and right and up and down
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0 and dfs(row, col): # and it has to be closed
                    count += 1
        
        return count
    
    def closedIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        count = 0

        def bfs(row, col):
            is_closed = True
            queue = deque([(row, col)])
            grid[row][col] = 1  # Mark the starting cell as visited

            while queue:
                r, c = queue.popleft()
                if r == 0 or r == rows - 1 or c == 0 or c == cols - 1: # cells at the border are not eligible
                    is_closed = False

                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    new_r, new_c = r + dr, c + dc
                    if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == 0:
                        grid[new_r][new_c] = 1
                        queue.append((new_r, new_c))

            return is_closed

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0 and bfs(row, col): # and it has to be closed
                    count += 1

        return count