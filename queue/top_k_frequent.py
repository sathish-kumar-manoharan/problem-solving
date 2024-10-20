from collections import Counter
import heapq

class Solution(object):
    def topKFrequent1(self, nums, k):
        """
        Time complexity : O(Nlog⁡k)
        Space complexity : O(N+k)
        """
        if len(nums) == k:
            return nums
        
        count = Counter(nums)
                
        return heapq.nlargest(k, count.keys(), key=count.get)
    
        """
        Time complexity : O(N)
        Space complexity : O(N)
        """
        def topKFrequent(self, nums, k):
            bucket = [[] for _ in range(len(nums)+1)]
            count = Counter(nums)
            
            for num, freq in count.items():
                bucket[freq].append(num)
            
            flat_list = [item for subList in bucket for item in subList]
            
            return flat_list[::-1][:k]