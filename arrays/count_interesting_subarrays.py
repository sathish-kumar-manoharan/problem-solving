class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        return self.atMost(nums, modulo, k) - self.atMost(nums, modulo, k-1)
    
    def atMost(self, nums, modulo, k):
        count = 0
        
        if not nums:
            return count
        
        start, window_size = 0, 0
        
        for end in range(len(nums)):
            window_size += 1 if nums[end] % modulo == k else 0
            
            while window_size > k:
                window_size -= 1 if nums[end] % modulo == k else 0
                start += 1
                
            count += end - start + 1
        
        return count