from typing import List

""""
https://leetcode.com/problems/interval-list-intersections
"""
class Solution:
    # Time: O(M + N)
    # Space: O(M + N)
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        intersections = []
        
        i = j = 0
        
        while i < len(firstList) and j < len(secondList):
            low = max(firstList[i][0], secondList[j][0])
            high = min(firstList[i][1], secondList[j][1])
            
            if low <= high:
                intersections.append([low, high])
                
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
                
        return intersections