from typing import List

"""
https://leetcode.com/problems/next-permutation
"""
class Solution:
    # Time: O(N)
    # Space: O(1)
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 2:
            return nums.reverse()
            
        i = len(nums) - 2
        
        while i >= 0 and nums[i+1] <= nums[i]:
            i -= 1

        if i >= 0:
            j = len(nums) - 1

            while nums[j] <= nums[i]:
                j -= 1

            nums[i], nums[j] = nums[j], nums[i]

        nums[i+1:] = reversed(nums[i+1:])
            