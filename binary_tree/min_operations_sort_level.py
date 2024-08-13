# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import List, Optional

from binary_tree.binary_tree import TreeNode

"""
https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/

BFS Traversal: 

O(N), where N is the number of nodes in the tree.
Min Swaps Calculation: For each level with L nodes, the time complexity is O(LlogL) due to sorting. In the worst case, summing over all levels gives us O(NlogN).
Overall Time Complexity: O(NlogN).

BFS Queue: O(N)
Level Values List: O(N)
Sorting and Swap Calculation: O(N)

"""

class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def min_swaps_to_sort(arr: List[int]) -> int:

            sorted_arr = sorted([(value, idx) for idx, value in enumerate(arr)])
            visited = [False] * len(arr)
            swaps = 0
            
            for i in range(len(arr)):
                # either visited or the element at the same index, then skip it
                if visited[i] or sorted_arr[i][1] == i:
                    continue
                
                cycle_size = 0
                x = i

                while not visited[x]:
                    visited[x] = True
                    x = sorted_arr[x][1]
                    cycle_size += 1
                
                if cycle_size > 1:
                    swaps += cycle_size - 1
            
            return swaps
        
        queue = deque([root])
        total_swaps = 0
        
        while queue:
            level_size = len(queue)
            level_values = []
            
            for _ in range(level_size):
                node = queue.popleft()
                level_values.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            total_swaps += min_swaps_to_sort(level_values)
        
        return total_swaps