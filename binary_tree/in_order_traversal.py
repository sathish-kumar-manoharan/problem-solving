
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    Morris traversal
    Time: O(N)
    Space: O(1)

    """
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        current = root

        while current:
            if not current.left:
                result.append(current.val)
                current = current.right
            else:
                prev = current.left

                while prev.right and prev.right != current:
                    prev = prev.right
                
                if not prev.right:
                    prev.right = current
                    current = current.left
                else:
                    prev.right = None
                    result.append(current.val)
                    current = current.right
    
        return result

    """
    Time: O(n)
    Space: O(N)
    """
    def inorderTraversal1(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        if not root:
            return  result

        stack = []
        current = root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            result.append(current.val)
            current = current.right

        return result