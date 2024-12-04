from collections import defaultdict
from typing import List

"""
https://leetcode.com/problems/subarrays-with-k-different-integers
Time: O(N)
Space: O(N)
"""
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        freq_map = defaultdict(int)
        left, total, current_count = 0, 0, 0

        for right in range(len(nums)):
            freq_map[nums[right]] += 1
            
            if freq_map[nums[right]] == 1:
                k -= 1

            if k < 0:
                freq_map[nums[left]] -= 1
                
                if freq_map[nums[left]] == 0:
                    k += 1
                left += 1
                current_count = 0

            if k == 0:
                while freq_map[nums[left]] > 1:
                    freq_map[nums[left]] -= 1
                    left += 1
                    current_count += 1

                total += (current_count + 1)

        return total

    def subarraysWithKDistinct1(self, nums: List[int], k: int) -> int:
        return self.atMost(nums, k) - self.atMost(nums, k-1)

    def atMost(self, nums, k):
        freq_map = defaultdict(int)
        left, total = 0, 0

        for right in range(len(nums)):
            freq_map[nums[right]] += 1
            
            while len(freq_map) > k:
                freq_map[nums[left]] -= 1

                if freq_map[nums[left]] == 0:
                    del freq_map[nums[left]]
                left += 1

            total += right - left + 1

        return total