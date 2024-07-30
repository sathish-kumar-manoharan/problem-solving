# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# https://leetcode.com/problems/closest-binary-search-tree-value/
from typing import Optional
from binary_tree.binary_tree import TreeNode

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        closest = root.val
        
        while root:
            #closest = min(root.val, closest, key = lambda x : (abs(target -x), x))

            if abs(target - root.val) < abs(target - closest):
                closest = root.val
                
            if abs(target - root.val) == abs(target - closest):
                closest = min(closest, root.val)
    
            root = root.left if target < root.val else root.right
                
        return closest