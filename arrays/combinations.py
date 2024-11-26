from typing import List

"""
https://leetcode.com/problems/combinations/
"""
class Solution:
    # Time: O(N!)
    # Space: O(K)
    def combine(self, n: int, k: int) -> List[List[int]]:      
        result = []
        stack = []

        def backtrack(start):
            if len(stack) == k:
                result.append(stack[:])
                return

            for num in range(start, n+1):
                stack.append(num)
                backtrack(num + 1)
                stack.pop()

        backtrack(1)

        return result
