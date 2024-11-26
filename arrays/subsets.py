from typing import List
"""
https://leetcode.com/problems/subsets

Time complexity: O(N × 2 ^N) to generate all subsets and then copy them into the output list.

Space complexity: O(N). We are using O(N) space to maintain curr, and are modifying curr in-place with backtracking. 
Note that for space complexity analysis, we do not count space that is only used for the purpose of returning output, so the output array is ignored.

"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        stack = []

        def backtrack(start):
            result.append(stack[:])

            for index in range(start, len(nums)):
                stack.append(nums[index])
                backtrack(index+1)
                stack.pop()

        backtrack(0)

        return result