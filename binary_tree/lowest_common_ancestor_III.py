"""
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii
Time: O(N)
Space: O(1)
"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class Solution:
    """
    Time: O(N)
    Space: O(1)
    """
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        a = p
        b = q

        while a != b:
            a = p if not a else a.parent
            b = q if not b else b.parent
        
        return a