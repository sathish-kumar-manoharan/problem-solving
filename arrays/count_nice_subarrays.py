from collections import deque
from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        sub_array_count, start, odd_count,current_count  = 0, 0, 0, 0

        for index in range(len(nums)):
            odd_count += nums[index] % 2

            if odd_count == k:
                current_count = 0
                while odd_count == k:
                    odd_count -= nums[start] % 2
                    start += 1
                    current_count += 1
            sub_array_count += current_count

        return sub_array_count
    
    def numberOfSubarrays1(self, nums: List[int], k: int) -> int:
        return self.atMost(nums, k) - self.atMost(nums, k-1)

    def atMost(self, nums, k):
        odd_count, window_size, start = 0, 0, 0

        for end in range(len(nums)):
            odd_count += nums[end] % 2

            while odd_count > k:
                odd_count -= nums[start] % 2
                start += 1

            window_size += end - start + 1

        return window_size

    def numberOfSubarrays2(self, nums: List[int], k: int) -> int:
        odd_indices = deque()
        subarrays = 0
        last_popped = -1
        initial_gap = 0

        for i in range(len(nums)):
            # If element is odd, append its index to the deque.
            if nums[i] % 2 == 1:
                odd_indices.append(i)
            # If the number of odd numbers exceeds k, remove the first odd index.
            if len(odd_indices) > k:
                last_popped = odd_indices.popleft()
            # If there are exactly k odd numbers, add the number of even numbers
            # in the beginning of the subarray to the result.
            if len(odd_indices) == k:
                initial_gap = odd_indices[0] - last_popped
                subarrays += initial_gap

        return subarrays