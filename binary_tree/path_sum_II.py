
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
https://leetcode.com/problems/path-sum-ii/
"""
class Solution:
    """
    Time: O(N)
    Space: O(N)
    """
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []

        def dfs(node, current_sum, path):
            if not node:
                return

            current_sum += node.val
            path.append(node.val)

            if not node.left and not node.right and current_sum == targetSum:
                result.append(list(path))
            else:
                dfs(node.left, current_sum, path)
                dfs(node.right, current_sum, path)

            path.pop()

        dfs(root, 0 , [])

        return result
    
    """
    Time: O(N^2)
    Space: O(N)
    """
    def pathSum1(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        
        if not root:
            return result

        
        def dfs(node, target, path):
            if not node:
                return

            if node.val - target == 0:
                path.append(node.val)
                result.append(path)
                return

            dfs(node.left, target - node.val, [*path, node.val])
            dfs(node.right, target - node.val, [*path, node.val])

        dfs(root, targetSum, [])

        return result

        