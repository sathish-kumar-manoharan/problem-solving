"""
https://leetcode.com/problems/kth-largest-element-in-an-array/
heap with sorting - O(n logK) + O(n-k logK)
however, they have asked how to do without sorting
which is O(N) and ON) for time and space

"""

from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        maximum = max(nums)
        minimum = min(nums)

        diff = minimum if minimum >= 0 else -minimum 

        buckets = [[] for _ in range(maximum + diff + 1)]

        for num in nums:
            buckets[num + diff].append(num)
        
        items = [item for subList in buckets for item in subList]
        
        return items[::-1][k-1]