
from collections import OrderedDict, deque
from typing import Optional
from binary_tree.binary_tree import TreeNode

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
https://leetcode.com/problems/binary-tree-pruning
"""
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        parent_map = OrderedDict()
        queue = deque([root])

        parent_map[root] = None

        while queue:
            node = queue.popleft()

            if node.left:
                queue.append(node.left)
                parent_map[node.left] = node

            if node.right:
                queue.append(node.right)
                parent_map[node.right] = node

        for node in reversed(parent_map):
            if node.val == 0 and not node.left and not node.right:
                parent = parent_map[node]

                if parent:
                    if parent.left == node:
                        parent.left = None
                    elif parent.right == node:
                        parent.right = None

        return root if root.val != 0 or root.left or root.right else None

    def pruneTree1(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
            return root
        
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)

        if root.val == 0 and not root.left and not root.right:
            return None

        return root