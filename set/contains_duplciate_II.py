from typing import List

"""
https://leetcode.com/problems/contains-duplicate-ii

Time complexity : O(n). We do n operations of search, delete and insert, each with constant time complexity.

Space complexity : O(min(n,k)). The extra space required depends on the number of items stored in the hash table, which is the size of the sliding window, 


"""

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()

        for i, num in enumerate(nums):
            if num in seen:
                return True
            seen.add(num)
            
            if len(seen) > k:
                seen.remove(nums[i - k])
        return False  