import heapq
from typing import List

"""
https://leetcode.com/problems/meeting-rooms-ii
Time: O(N log N) for sorting
Space: O(N) for heap
"""
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        free_rooms = []
        
        intervals.sort(key=lambda x: x[0])
                
        for interval in intervals:
            if free_rooms and free_rooms[0] <= interval[0]:
                heapq.heappop(free_rooms)
                
            heapq.heappush(free_rooms, interval[1])
            
        return len(free_rooms)