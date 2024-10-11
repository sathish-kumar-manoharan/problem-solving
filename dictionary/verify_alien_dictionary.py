"""
https://leetcode.com/problems/verifying-an-alien-dictionary
Time: O(N)
Space: O(1)
"""

from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if not words:
            return False
        
        lookup = { char : index for index, char in enumerate(order)}
        
        for i in range(len(words)-1):
            for j in range(len(words[i])):
                
                if j >= len(words[i+1]):
                    return False
                
                if words[i][j] != words[i+1][j]:
                    if lookup[words[i][j]] > lookup[words[i+1][j]]:
                        return False
                    break
        
        return True