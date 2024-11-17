from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
https://leetcode.com/problems/path-sum/
Time complexity : we visit each node exactly once, thus the time complexity is O(N), where N is the number of nodes.
Space complexity : in the worst case, the tree is completely unbalanced, 
e.g. each node has only one child node, the recursion call would occur N times (the height of the tree),
therefore the storage to keep the call stack would be O(N). But in the best case (the tree is completely balanced),
the height of the tree would be log(N). Therefore, the space complexity in this case would be O(log(N)).
"""
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        queue = [(root, targetSum - root.val)]

        while queue:
            node, balance = queue.pop()

            if not node.left and not node.right and balance == 0:
                return True

            if node.left:
                queue.append((node.left, balance-node.left.val))

            if node.right:
                queue.append((node.right, balance-node.right.val))

        return False


    def hasPathSum1(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right and targetSum - root.val == 0:
            return True
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)

