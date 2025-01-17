"""
https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
"""

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Time: O(N)
    # Space: O(1)
    def flatten(self, root: TreeNode) -> None:
        # Handle the null scenario
        if not root:
            return None

        node = root
        while node:

            # If the node has a left child
            if node.left:

                # Find the rightmost node
                rightmost = node.left
                while rightmost.right:
                    rightmost = rightmost.right

                # rewire the connections
                rightmost.right = node.right
                node.right = node.left
                node.left = None

            # move on to the right side of the tree
            node = node.right

    # Time: O(N)
    # Space: O(N)
    def flatten(self, root: Optional[TreeNode]) -> None:
        def dfs(node):
            if not node:
                return None

            if not node.left and not node.right:
                return node

            left_tail = dfs(node.left)

            right_tail = dfs(node.right)

            if left_tail:
                left_tail.right = node.right
                node.right = node.left
                node.left = None

            return right_tail if right_tail else left_tail

        dfs(root)