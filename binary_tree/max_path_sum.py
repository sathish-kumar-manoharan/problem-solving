# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
from typing import Optional

from binary_tree.binary_tree import TreeNode

"""
https://leetcode.com/problems/binary-tree-maximum-path-sum/
Time: O(N)
Space: O(N)
"""
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = -math.inf
        
        def helper(node):
            if not node:
                return 0
            
            max_left_sum = max(helper(node.left), 0)
            max_right_sum = max(helper(node.right), 0)
            
            current_sum = node.val + max_left_sum + max_right_sum
            
            self.maxSum = max(self.maxSum, current_sum)
            
            return node.val + max(max_left_sum, max_right_sum)
        
        helper(root)
        
        return self.maxSum