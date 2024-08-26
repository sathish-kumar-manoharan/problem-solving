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
https://leetcode.com/problems/binary-tree-right-side-view/
"""
class Solution:
    """
    Time complexity: O(N) since one has to visit each node.
    Space complexity: O(D) to keep the queues, where D is a tree diameter. 
    Let's use the last level to estimate the queue size. This level could contain up to N/2 tree nodes in the case of complete binary tree.
    """
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        rightSideView = []
        
        if not root:
            return rightSideView
        
        queue = deque([root])

        level = 0
        
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                
                if len(rightSideView) == level:
                    rightSideView.append(node.val)
                
                if node.right:
                    queue.append(node.right)
                    
                if node.left:
                    queue.append(node.left)
            
            level += 1
                
        return rightSideView
            
    """
    Time complexity: O(N) since one has to visit each node.
    Space complexity: O(H) to keep the recursion stack, where H is a tree height. The worst-case situation is a skewed tree when H=N.
    """
    def rightSideView_dfs(self, root: Optional[TreeNode]) -> List[int]:
        rightSideView = []
        
        if not root:
            return rightSideView
        
        
        def dfs(node, depth):
            if not node:
                return
            
            if len(rightSideView) == depth:
                rightSideView.append(node.val)
            
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
        
        dfs(root, 0)
        
        return rightSideView