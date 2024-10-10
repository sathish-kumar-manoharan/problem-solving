from typing import List

#Time: O(N)
#Space: O(1)
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        max_robbed = 0
        max_robbed_next = 0
        
        for index in range(len(nums)):
            current = max(max_robbed, max_robbed_next + nums[index])
            
            max_robbed_next = max_robbed
            max_robbed = current
            
        
        return max_robbed
    

#Time: O(N)
#Space: O(N)
    def rob1(self, nums: List[int]) -> int:

        # Special handling for empty case.
        if not nums:
            return 0

        maxRobbedAmount = [None for _ in range(len(nums) + 1)]
        N = len(nums)

        # Base case initialization.
        maxRobbedAmount[N], maxRobbedAmount[N - 1] = 0, nums[N - 1]

        # DP table calculations.
        for i in range(N - 2, -1, -1):

            # Same as recursive solution.
            maxRobbedAmount[i] = max(
                maxRobbedAmount[i + 1], maxRobbedAmount[i + 2] + nums[i]
            )

        return maxRobbedAmount[0]