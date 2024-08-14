""""
https://leetcode.com/problems/contains-duplicate-iii

Time complexity: 
O(n). For each of the n elements, we do at most three searches, one insert, and one delete on the HashMap, which costs constant time on average. Thus, the entire algorithm costs O(n) time.

Space complexity: O(min(n,k)). Space is dominated by the HashMap, which is linear to the size of its elements. The size of the HashMap is upper bounded by both n and k. Thus the space complexity is O(min(n,k)).
"""

from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        if valueDiff < 0:
            return False
        
        buckets = {}
        
        width = valueDiff + 1  # Increment by 1 to handle the range correctly
        
        for index in range(len(nums)):
            bucket = self.get_id(nums[index], width)
            
            # Check if current bucket is empty, each bucket may contain at most one element
            if bucket in buckets:
                return True
            
            # Check the neighbor buckets for almost duplicates
            if bucket - 1 in buckets and abs(nums[index] - buckets[bucket - 1]) < width:
                return True
            
            if bucket + 1 in buckets and abs(nums[index] - buckets[bucket + 1]) < width:
                return True
            
            # Now bucket is empty and no almost duplicates in neighbor buckets
            buckets[bucket] = nums[index]
            
            # to maintain a sliding window of size indexDiff over the nums list.
            if index >= indexDiff:
                del buckets[self.getID(nums[index - indexDiff], width)]
                
        return False
    
    # Get the ID of the bucket from element value x and bucket width w
    # Division '/' in Python with '//' performs floor division, which is necessary for correct bucketing.
    # Floor division to handle both positive and negative integers correctly
    def get_id(self, x, w):
        return x // w 