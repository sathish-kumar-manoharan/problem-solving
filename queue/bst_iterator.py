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