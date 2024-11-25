
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
https://leetcode.com/problems/binary-tree-vertical-order-traversal/
Time: O(N)
Space: O(N)
"""

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        if not root:
            return result

        lookup = defaultdict(list)
        queue = deque([(root, 0)])

        min_col, max_col = 0, 0

        while queue:
            for _ in range(len(queue)):
                node, col = queue.popleft()

                lookup[col].append(node.val)

                if node.left:
                    queue.append((node.left, col-1))
                    min_col = min(min_col, col-1)

                if node.right:
                    queue.append((node.right, col+1))
                    max_col = max(max_col, col+1)

        for index in range(min_col, max_col+1):
            result.append(lookup[index])

        return result



