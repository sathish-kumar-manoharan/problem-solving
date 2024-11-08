
from collections import OrderedDict, deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
https://leetcode.com/problems/binary-tree-pruning
"""
def printTree(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val if node else 'null')
            
            if node:
                queue.append(node.left)
                queue.append(node.right)

        result.append(current_level)

    print(result)

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

def pruneTree1(root: Optional[TreeNode]) -> Optional[TreeNode]:
    
    if not root:
        return root
    
    root.left = pruneTree1(root.left)
    root.right = pruneTree1(root.right)

    if root.val == 0 and not root.left and not root.right:
        return None

    return root
    
root = TreeNode(1)
root.right = TreeNode(0)
root.right.left = TreeNode(0)
root.right.right = TreeNode(1)

printTree(root)
printTree(pruneTree1(root))