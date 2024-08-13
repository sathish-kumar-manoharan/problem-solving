# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import List, Optional

from binary_tree.binary_tree import TreeNode

"""
https://leetcode.com/problems/binary-tree-level-order-traversal/

Time complexity: O(N) since each node is processed exactly once.
Space complexity: O(N) to keep the output structure which contains N node values.
"""

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        
        if not root:
            return levels
        
        queue = deque([root])
        
        level = 0
        
        while queue:
            size = len(queue)
            
            for _ in range(size):
            
                node = queue.popleft()

                if level == len(levels):
                    levels.append([])
                    
                levels[level].append(node.val)
                
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
                    
            level += 1
            
        return levels
            
        
        
    def levelOrderDfs(self, root: Optional[TreeNode]) -> List[List[int]]:    
        levels = []
        
        def dfs(node, level):
            if not node:
                return
            
            if level == len(levels):
                levels.append([])
                
            levels[level].append(node.val)
            
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        
        
        dfs(root, 0)
        
        return levels