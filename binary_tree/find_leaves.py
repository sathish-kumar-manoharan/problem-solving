# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# https://leetcode.com/problems/find-leaves-of-binary-tree/

from typing import List, Optional
from binary_tree.binary_tree import TreeNode

"""
Time Complexity: Assuming 
𝑁 is the total number of nodes in the binary tree, traversing the tree takes 
O(N) time and storing all the pairs at the correct position also takes 
O(N) time. Hence overall time complexity of this approach is O(N).

Space Complexity: 
O(N), the space used by the recursion call stack.
"""
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        leaves = []
        
        if not root:
            return leaves
        
        def dfs(node):
            if not node:
                return -1
                       
            height = max(dfs(node.left),  dfs(node.right)) + 1
            
            if height == len(leaves):
                leaves.append([])
                
            leaves[height].append(node.val)
            
            return height
            
        dfs(root)
        
        return leaves