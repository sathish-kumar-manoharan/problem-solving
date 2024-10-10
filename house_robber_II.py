from typing import List
# https://leetcode.com/problems/house-robber-ii
#Time: O(N)
#Space: O(1)
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        def rob_max(nums):          
            max_robbed = 0
            max_robbed_next = 0
            
            for num in nums:
                current = max(max_robbed, max_robbed_next + num)
                
                max_robbed_next = max_robbed
                max_robbed = current
                
            return max_robbed
        
        return max(rob_max(nums[1:]), rob_max(nums[:-1]))