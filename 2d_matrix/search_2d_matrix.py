from typing import List
"""
https://leetcode.com/problems/search-a-2d-matrix/
using binary search O(log(m*n))
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        left , right = 0, rows *cols -1

        while left <= right:
            mid = left + (right - left) //2
            element = matrix[mid//cols][mid % cols]

            if element == target:
                return True

            if element < target:
                left = mid + 1

            else:
                right = mid - 1

        return False