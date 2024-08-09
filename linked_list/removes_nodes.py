# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from linked_list.ListNode import ListNode

"""
https://leetcode.com/problems/remove-nodes-from-linked-list/

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # T: O(3N) -> O(N), Where N is the number of nodes
    # S: O(1), No additional variables required
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = self.reverse(head)
        
        maximum = 0
        prev = None
        current = head
        
        while current:
            maximum = max(maximum, current.val)
            
            if current.val < maximum:
                prev.next = current.next
                deleted = current
                current = current.next
                deleted.next = None
            else:
                prev = current
                current = current.next
        
        return self.reverse(head)
        
    
    def reverse(self, head):
        prev = None
        current = head
        
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            
        return prev
        
        
    # T: O(N), Where N is the number of nodes
    # S: O(N), Where N is the number of nodes
    def removeNodes1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        next_node = self.removeNodes(head.next)
        
        if head.val < next_node.val:
            return next_node
        
        head.next = next_node
        
        return head