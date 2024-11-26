from typing import List

"""
https://leetcode.com/problems/rotate-image/
"""
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])

        for row in range(rows):
            for col in range(row +1, cols):
                 matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

        for row in range(rows):
            for col in range(cols//2):
                 # -1, which refers to the last element in the row. 
                 # If col is 1, -col-1 would be -2, which refers to the second-to-last element in the row, and so on.
                matrix[row][col], matrix[row][-col-1] = matrix[row][-col-1], matrix[row][col]