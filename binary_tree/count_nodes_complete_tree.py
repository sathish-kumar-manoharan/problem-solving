"""
https://leetcode.com/problems/count-complete-tree-nodes/
"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        depth = self.getDepth(root)

        if depth == 0:
            return 1

        left, right = 1, 2** depth -1

        while left <= right:
            mid = left + (right - left) //2

            if self.exists(mid, depth, root):
                left = mid + 1
            else:
                right = mid - 1

        return (2 ** depth - 1) + left

    def exists(self, index, depth, node):
        left, right = 0, 2** depth -1

        for _ in range(depth):
            mid = left + (right - left) //2

            if index <= mid:
                node = node.left
                right = mid
            else:
                node = node.right
                left = mid + 1

        return node is not None

    def getDepth(self, node):
        depth = 0  
        
        if not node:
            return depth

        while node.left:
            node = node.left
            depth += 1

        return depth

    def countNodes1(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_depth = self.getLeftDepth(root)
        right_depth = self.getRightDepth(root)

        if left_depth == right_depth:
            return 2 ** left_depth -1

        return self.countNodes(root.left) + self.countNodes(root.right) + 1

    def getLeftDepth(self, node):
        if not node:
            return 0

        return 1 + self.getLeftDepth(node.left) 

    def getRightDepth(self, node):
        if not node:
            return 0

        return 1 + self.getRightDepth(node.right) 
