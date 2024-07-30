# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# https://leetcode.com/problems/merge-two-sorted-lists/

from typing import Optional

from linked_list.ListNode import ListNode


class Solution:
    # T:O(N + M), where N, is the number of the nodes in the list1 and M is the size of list2
    # S:O(1), no additional space required
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        
        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
                
            current = current.next
            
        current.next = list2 if not list1 else list1
        
        return dummy.next
        
    # T:O(N + M), where N, is the number of the nodes in the list1 and M is the size of list2
    # S:O(N + M), is the stack size for the recursion calls
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1
        elif list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2