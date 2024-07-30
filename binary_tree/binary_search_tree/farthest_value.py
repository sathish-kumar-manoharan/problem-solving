# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
from binary_tree.binary_tree import TreeNode

class Solution:
    def farthestValue(self, root: Optional[TreeNode], target: float) -> int:
        farthest = root.val
        
        while root:
            farthest = max(root.val, farthest, key = lambda x : (abs(target -x), x))
    
            root = root.left if target < root.val else root.right
                
        return farthest