"""
https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    Morris traversal algorithm
    Time: O(N)
    Space: O(1)
    """
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None

        first, last = None, None
        current = root

        while current:
            if not current.left:
                # Process the current node
                if last:
                    last.right = current
                    current.left = last
                else:
                    first = current
                last = current

                # Move to the right child
                current = current.right
            else:
                # Find the inorder predecessor
                predecessor = current.left
                while predecessor.right and predecessor.right != current:
                    predecessor = predecessor.right

                if not predecessor.right:
                    # Link the predecessor to the current node
                    predecessor.right = current
                    current = current.left
                else:
                    # Revert the changes in the tree structure
                    predecessor.right = None

                    # Process the current node
                    if last:
                        last.right = current
                        current.left = last
                    else:
                        first = current
                    last = current

                    # Move to the right child
                    current = current.right

        # Make the doubly linked list circular
        last.right = first
        first.left = last

        return first

    """
    in order traversal algorithm
    Time: O(N)
    Space: O(H) -> O(N)
    """
    def treeToDoublyList1(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        first, last = None, None

        def dfs(node):
            if not node:
                return

            nonlocal last, first

            # left
            dfs(node.left)

            # node 
            if last:
                # link the previous node (last)
                # with the current one (node)
                last.right = node
                node.left = last
            else:
                # keep the smallest node
                # to close DLL later on
                first = node   

            last = node

            # right
            dfs(node.right)        
       
        dfs(root)

        # make it circular
        last.right = first
        first.left = last

        return first