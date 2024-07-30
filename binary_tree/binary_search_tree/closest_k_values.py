# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# https://leetcode.com/problems/closest-binary-search-tree-value-ii

from collections import deque
from typing import List, Optional
from binary_tree.binary_tree import TreeNode

class Solution:
    # T: O(N)
    # S: O(N + K) , We use O(n) space for the recursion call stack and O(k) space for queue
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        closest = deque()
        
        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            
            closest.append(node.val)
            
            if len(closest) > k:
                if abs(target - closest[0] <= abs(target - closest[-1])):
                    closest.pop()
                    return
                else:
                    closest.popleft()
            
            dfs(node.right)
        
        dfs(root)
        
        return closest
        
    # T: O(N + Log(N-k) + K)
    # S: O(N)
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        closest = []
        
        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            closest.append(node.val)
            dfs(node.right)
            
        dfs(root)
        
        left, right = 0, len(closest)-k
        
        while left < right:
            mid = left + (right - left) // 2
            
            if abs(target - closest[mid+k]) < abs(target - closest[mid]):
                left = mid + 1
            else:
                right = mid
        
        return closest[left : left+k]
        
    # T: O(N * Log N)
    # S: O(N)
    def closestKValues1(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        closest = []
        
        def dfs(node):
            if not node:
                return
            
            closest.append(node.val)
            
            dfs(node.left)
            dfs(node.right)
            
        
        dfs(root)
        
        closest.sort(key = lambda x: (abs(target - x), x))
        
        return closest[:k]
        
        