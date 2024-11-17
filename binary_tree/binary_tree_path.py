
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
https://leetcode.com/problems/binary-tree-paths/
"""        
class Solution:
    """
    Time: O(N), since list is not created again and again, its reused and path.pop() removes the extra path added for left and right for each node
    Space: O(N)
    """
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []

        if not root:
            return result

        def dfs(node, path):
            if not node:
                return

            path.append(str(node.val))

            if not node.left and not node.right:
                result.append('->'.join(path))
            else:
                dfs(node.left, path)
                dfs(node.right, path)

            path.pop()

        dfs(root, [])

        return result

    """
    Time: O(N^2)
    Space: O(N)
    """
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []

        if not root:
            return result

        def dfs(node, path):
            if not node:
                return

            path.append(node.val)

            if not node.left and not node.right:
                result.append('->'.join(map(str, path)))
                return

            dfs(node.left, [*path])
            dfs(node.right, [*path])

        dfs(root, [])

        return result
