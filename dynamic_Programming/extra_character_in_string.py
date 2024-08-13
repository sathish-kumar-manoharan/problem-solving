"""
https://leetcode.com/problems/extra-characters-in-a-string/
"""
from functools import cache
from typing import List

"""
Let 
𝑁 be the total characters in the string. Let 
𝑀 be the average length of the strings in dictionary. Let 
𝐾 be the length of the dictionary.

Time complexity: 
O(N ^2 +M⋅K). 
The two nested for loops that are being used for the dynamic programming operation cost 
Building the trie costs O(M⋅K).

Space complexity: 
O(N+M⋅K). 
The Trie used to store the strings in dictionary will incur a cost of O(M⋅K).
The dp method will consume stack space and traverse to a depth of N, resulting in a cost of O(N).

"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        root = self.build_tree(dictionary)
    
        @cache
        def dfs(start):
            if start == len(s):
                return 0
            
            min_count = 1 + dfs(start + 1)
            
            node = root
            
            for end in range(start, len(s)):
                if s[end] not in node.children:
                    break
                
                node = node.children[s[end]]
                
                if node.isWord:
                    min_count = min(min_count, dfs(end + 1))
    
            return min_count
        
        return dfs(0)
    
    
    def build_tree(self, dictionary):
        root = TrieNode()
        
        for word in dictionary:
            current = root
            
            for char in word:
                if char not in current.children:
                    current.children[char] = TrieNode()
            
                current = current.children[char]
            
            current.isWord = True
        
        return root
    
    """
    Let 
    𝑁 be the total characters in the string. Let 
    𝑀 be the average length of the strings in dictionary. Let 
    𝐾 be the length of the dictionary.

    Time complexity: 
    N+1 unique states of the dp method. In each state of dp, we iterate over end, which is 
    O(N) iterations. In each of these iterations, we create a substring, which costs 
    O(N). Hence, the overall cost of the dp method is 
    O(N^3).

    Space complexity: 
    O(N+M⋅K). The HashSet used to store the strings in the dictionary will incur a cost of 
    O(M⋅K). Additionally, the dp method will consume stack space and traverse to a depth of 𝑁
    N in the worst case scenario, resulting in a cost of O(N).
    """
    def minExtraChar1(self, s: str, dictionary: List[str]) -> int:
        dictionary_set = set(dictionary)
        
        @cache
        def dfs(start):
            if start == len(s):
                return 0
            
            min_count = 1 + dfs(start + 1)
            
            for end in range(start, len(s)):
                if s[start : end + 1] in dictionary_set:
                    min_count = min(min_count, dfs(end + 1))
                    
            return min_count
        
        return dfs(0)