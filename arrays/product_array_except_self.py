"""
https://leetcode.com/problems/product-of-array-except-self
Time: O(n)
Space:(1)

"""
from typing import List

class Solution:
    """
    Time: O(n)
    Space: O(1)
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = [1]* len(nums)

        for index in range(1, len(nums)):
            product[index] = product[index-1] * nums[index-1]

        multiplier = 1

        for index in reversed(range(len(nums))):
            print(index)
            product[index] = product[index] * multiplier
            multiplier *= nums[index]
            
        return product

    """
    Time: O(N)
    Space:O(N)
    """
    def productExceptSelf1(self, nums: List[int]) -> List[int]:
        left = [1]* len(nums)

        for index in range(1, len(nums)):
            left[index] = left[index-1] * nums[index-1]

        right = [1]* len(nums)

        for index in range(len(nums)-2, -1, -1):
            right[index] = right[index+1] * nums[index+1]

        product = []

        for index in range(len(nums)):
            product.append(left[index] * right[index])

        return product
