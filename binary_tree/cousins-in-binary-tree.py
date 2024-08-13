# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import Optional

from binary_tree.binary_tree import TreeNode

""""
https://leetcode.com/problems/cousins-in-binary-tree/solution/

Time : O(N), Where N is the number of nodes
Space: O(H) for DFS which can be N on worst case scenario
The space complexity of the BFS approach is O(N), where N is the number of nodes in the binary tree.

The reason for this is:

The queue used in the BFS traversal can hold at most the number of nodes in the widest level of the tree.
In the worst case, the widest level of the tree can have up to N/2 nodes (assuming a complete binary tree).
Therefore, the maximum size of the queue, and hence the space complexity, is O(N/2) = O(N).

"""
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
		# store (parent, depth) tuple
        res = []
		
		# bfs
        queue = deque([(root, None, 0)])        
        
        while queue:
			# minor optimization to stop early if both targets found
            if len(res) == 2:
                break
                
            node, parent, depth = queue.popleft()
            
            # if target found
            if node.val == x or node.val == y:
                res.append((parent, depth))
                
            if node.left:
                queue.append((node.left, node, depth + 1))
            if node.right:
                queue.append((node.right, node, depth + 1))

		# unpack two nodes
        node_x, node_y = res[0], res[1]
		
        # compare and decide whether two nodes are cousins		
        return node_x[0] != node_y[0] and node_x[1] == node_y[1]
                
    
    def isCousins_dfs(self, root: Optional[TreeNode], x: int, y: int) -> bool:
		# store (parent, depth) tuple
        res = [] 
        
		# dfs
        def dfs(node, parent, depth):
            if not node:
                return
            
            if node.val == x or node.val == y:
                res.append((parent, depth))
                
            dfs(node.left, node, depth + 1)
            dfs(node.right, node, depth + 1)
            
        dfs(root, None, 0)

		# unpack two nodes found
        node_x, node_y = res[0], res[1]
		
        # compare and decide whether two nodes are cousins
        return node_x[0] != node_y[0] and node_x[1] == node_y[1]
