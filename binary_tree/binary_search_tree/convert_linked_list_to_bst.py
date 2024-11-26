
from typing import Optional

from linked_list import ListNode

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Time: O(N)
    # Space: O(log N)
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        size = self.findSize(head)

        def dfs(left, right):
            nonlocal head
            
            if left > right:
                return None

            mid = left + (right - left) //2

            left = dfs(left, mid -1)

            node = TreeNode(head.val)

            node.left = left

            head = head.next

            node.right = dfs(mid+1, right)

            return node

        return dfs(0, size-1)

    
    def findSize(self, node):
        count = 0

        while node:
            node = node.next
            count += 1

        return count