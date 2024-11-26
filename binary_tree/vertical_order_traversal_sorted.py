# Definition for a binary tree node.
from collections import defaultdict, deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        if not root:
            return result

        lookup = defaultdict(list)
        queue = deque([(root, 0)])

        level, min_col, max_col = 0, 0, 0
        
        while queue:
            for _ in range(len(queue)):
                node, col = queue.popleft()

                lookup[col].append((level, node.val))

                if node.left:
                    queue.append((node.left, col-1))
                    min_col = min(min_col, col-1)

                if node.right:
                    queue.append((node.right, col+1))
                    max_col = max(max_col, col+1)
            level += 1

        for index in range(min_col, max_col+1):
            result.append([val for _, val in sorted(lookup[index])])

        return result
