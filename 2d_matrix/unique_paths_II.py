from typing import List

"""
https://leetcode.com/problems/unique-paths-ii/
Time: O(M*N)
Space: O(M*N)
"""
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1 or obstacleGrid[rows-1][cols-1] == 1:
            return 0

        dp = [ [0 for _ in range(cols)] for _ in range(rows)]
        
        for row in range(rows):
            if obstacleGrid[row][0] == 1:
                break
            dp[row][0] = 1

        for col in range(cols):
            if obstacleGrid[0][col] == 1:
                break
            dp[0][col] = 1

        for row in range(1, rows):
            for col in range(1, cols):
                if obstacleGrid[row][col] == 0:
                        dp[row][col] = dp[row-1][col] + dp[row][col-1]
        
        return dp[rows-1][cols-1]