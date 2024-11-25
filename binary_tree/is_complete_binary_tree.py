"""
https://leetcode.com/problems/check-completeness-of-a-binary-tree/
"""
from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Time: O(N)
    # Space: O(N)
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = [(root, 0, 0)]
        position = 1
        
        while queue:
            node, level, column = queue.pop(0)
            if position != 2 ** level + column:
                return False

            if node.left:
                queue.append((node.left, level + 1, column * 2))
            if node.right:
                queue.append((node.right, level + 1, column * 2 + 1))

            position += 1

        return True

    # Time: O(N)
    # Space: O(N)
    def isCompleteTree1(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        queue = deque([root])

        while queue and queue[0]: 
            node = queue.popleft()

            queue.append(node.left)
            queue.append(node.right)

        while queue and not queue[0]:
            queue.popleft()

        return len(queue) == 0