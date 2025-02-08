"""
https://leetcode.com/problems/add-two-numbers/
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

from typing import Optional

class Solution:
    # Time: O(max(M, N))
    # Space: O(1)
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]: # type: ignore
        dummy = ListNode(0)

        current = dummy
        carry = 0

        while l1 != None or l2 != None or carry != 0:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            sum = v1 + v2 + carry
            carry = sum // 10

            new_node = ListNode(sum % 10)
            
            current.next = new_node
            current = new_node

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
