""""
https://leetcode.com/problems/remove-nth-node-from-end-of-list
"""
from typing import Optional

from linked_list import ListNode

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        slow = dummy
        fast = dummy

        for _ in range(n+1):
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next

    def removeNthFromEnd1(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0

        dummy = ListNode(0)
        dummy.next = head

        current = head

        while current:
            length += 1
            current = current.next

        length -= n

        current = dummy

        while length > 0:
            length -= 1
            current = current.next

        current.next = current.next.next

        return dummy.next