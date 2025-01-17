from typing import List
"""
https://leetcode.com/problems/subsets-ii

Time complexity: O(N × 2 ^N) to generate all subsets and then copy them into the output list.

Space complexity: O(N). We are using O(N) space to maintain curr, and are modifying curr in-place with backtracking. 
Note that for space complexity analysis, we do not count space that is only used for the purpose of returning output, so the output array is ignored.

"""
class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()

        subsets = [[]]
        subsetSize = 0

        for i in range(len(nums)):
            startingIndex = subsetSize if i >= 1 and nums[i] == nums[i - 1] else 0
            subsetSize = len(subsets)
            
            for j in range(startingIndex, subsetSize):
                currentSubset = list(subsets[j])
                currentSubset.append(nums[i])
                subsets.append(currentSubset)

        return subsets

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
   
        result = []
        stack = []

        def backtrack(start):
            result.append(stack[:])

            for index in range(start, len(nums)):
                if index != start and nums[index] == nums[index-1]:
                    continue

                stack.append(nums[index])
                backtrack(index+1)
                stack.pop()

        backtrack(0)

        return result

    