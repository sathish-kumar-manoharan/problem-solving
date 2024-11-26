"""
https://leetcode.com/problems/binary-search-tree-iterator
Time:
    Constructor - O(N)
    next() - O(1)
    hasNext - O(1)
Space: O(N) for the queue
"""
from collections import deque
from typing import Optional
from binary_tree.binary_tree import TreeNode


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.queue = deque()
        self.inOrder(root)
    
    def inOrder(self, node):
        if not node:
            return
        
        self.inOrder(node.left)
        self.queue.append(node.val)
        self.inOrder(node.right)

    def next(self) -> int:
        return self.queue.popleft()

    def hasNext(self) -> bool:
        return len(self.queue) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x: int):
#         self.val = x
#         self.left = None
#         self.right = None


class BSTIterator:

    def __init__(self, root: TreeNode) -> None:

        # Stack for the recursion simulation
        self.stack = []

        # Remember that the algorithm starts with a call to the helper function
        # with the root node as the input
        self._leftmost_inorder(root)

    def _leftmost_inorder(self, root: TreeNode) -> None:
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        # Node at the top of the stack is the next smallest element
        topmost_node = self.stack.pop()

        # Need to maintain the invariant. If the node has a right child, call the
        # helper function for the right child
        if topmost_node.right:
            self._leftmost_inorder(topmost_node.right)
        return topmost_node.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0