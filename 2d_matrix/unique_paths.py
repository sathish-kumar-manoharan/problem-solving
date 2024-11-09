from typing import List

"""
https://leetcode.com/problems/unique-paths/
Time: O(M*N)
Space: O(M*N)
"""
class Solution:
    # Time: O(M*N)
    # Space: O(M)
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * m

        for _ in range(1, n):
            for index in range(1, m):
                dp[index] += dp[index-1]

        return dp[-1]
    
    # Time: O(M*N)
    # Space: O(min(M*N))
    def uniquePaths(self, m: int, n: int) -> int:
        if m > n:
            m, n = n, m

        dp = [1] * m

        for _ in range(1, n):
            for index in range(1, m):
                dp[index] += dp[index-1]

        return dp[-1]

    # Time: O(M*N)
    # Space: O(M*N)
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]

        for row in range(1, m):
            for col in range(1, n):
                dp[row][col] = dp[row-1][col] + dp[row][col-1]

        return dp[m-1][n-1]