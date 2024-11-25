
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    using heap add all the items in to heap
    take items from the heap and form a linked List
    Time: O(N log K)
    Space: O(N), to store the elements in Heap

    So we can pick two lists at a time and keep merging them in O(N) time complexity
    Time: O(N) + O(N) = O(N)
    Space: O(1)
    """
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        for index in range(1, len(lists), 1):
            lists[index] = self.merge2Lists(lists[index-1], lists[index])

        return lists[-1]

    """
    Merging 2 list and keep merging list using binary search that takes log K time complexity
    Time : O(N log K)
    Space: O(log K), recurision depth is log K, where K is the number of lists present.
    """
    def mergeKLists1(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        return self.splitLists(lists, 0, len(lists)-1)

    def splitLists(self, lists, left, right):
        if left == right:
            return lists[left]

        if left > right:
            return None

        mid = left + (right - left) // 2
        
        left = self.splitLists(lists, left, mid)
        right = self.splitLists(lists, mid+1, right)

        return self.merge2Lists(left, right)

    def merge2Lists(self, l1, l2):
        dummy = ListNode(-1)
        current = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            
            current = current.next
        
        current.next = l1 if l1 else l2

        return dummy.next