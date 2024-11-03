"""
https://leetcode.com/problems/even-odd-tree/
Time: O(N)
Space: O(N)
"""
from collections import deque
import math
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        queue = deque([root])
        level = 0

        while queue:
            size = len(queue)
            prev = math.inf

            even = level % 2 == 0

            if even:
                prev = -prev

            while size > 0:
                current = queue.popleft()

                if ((even and (current.val % 2 == 0 or current.val <= prev)) or
                    (not even and (current.val % 2 == 1 or current.val >= prev))):
                    return False

                prev = current.val

                if current.left:
                    queue.append(current.left)
                
                if current.right:
                    queue.append(current.right)

                size -= 1

            level += 1

        return True

    def isEvenOddTree1(self, root: Optional[TreeNode]) -> bool:
        prev = []

        def dfs(node, level):
            if not node:
                return True
            
            if node.val % 2 == level % 2:
                return False

            while len(prev) <= level:
                prev.append(0)

            if (prev[level] != 0 and 
                    ((level % 2 == 0 and prev[level] >= node.val) or
                     (level % 2 == 1 and prev[level] <= node.val))):
                return False

            prev[level] = node.val

            return dfs(node.left, level + 1) and dfs(node.right, level + 1)

        return dfs(root, 0)
