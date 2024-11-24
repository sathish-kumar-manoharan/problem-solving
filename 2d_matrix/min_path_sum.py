from typing import List

"""
https://leetcode.com/problems/minimum-path-sum/
"""
class Solution:
    # Time: O(M*N)
    # Space: O(min(M,N))
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        if cols > rows:
            rows, cols = rows, cols

        dp = [0] * cols  # 1D array for storing current row's path sums

        # Initialize the first cell
        dp[0] = grid[0][0]

        # Initialize the first row
        for col in range(1, cols):
            dp[col] = dp[col - 1] + grid[0][col]

        # Compute the path sums for the rest of the grid
        for row in range(1, rows):
            dp[0] += grid[row][0]
            for col in range(1, cols):
                dp[col] = grid[row][col] + min(dp[col], dp[col - 1])

        return dp[-1] 

    # Time: O(M*N)
    # Space: O(N)
    def minPathSum2(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        dp = [0] * cols  # 1D array for storing current row's path sums

        # Initialize the first cell
        dp[0] = grid[0][0]

        # Initialize the first row
        for col in range(1, cols):
            dp[col] = dp[col - 1] + grid[0][col]

        # Compute the path sums for the rest of the grid
        for row in range(1, rows):
            dp[0] += grid[row][0]
            for col in range(1, cols):
                dp[col] = grid[row][col] + min(dp[col], dp[col - 1])

        return dp[-1] 

    # Time: O(M*N)
    # Space: O(M*N)
    def minPathSum1(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
    
        dp = [[0] *cols for _ in range(rows)]

        dp[0][0] = grid[0][0]

        for col in range(1, cols):
            dp[0][col] = dp[0][col-1] + grid[0][col]

        for row in range(1, rows):
            dp[row][0] = dp[row-1][0] + grid[row][0]

        for row in range(1, rows):
            for col in range(1, cols):
                dp[row][col] = grid[row][col] + min(dp[row-1][col], dp[row][col-1])

        return dp[rows-1][cols-1]