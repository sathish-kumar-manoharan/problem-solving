from typing import List
"""
https://leetcode.com/problems/longest-common-prefix/
Time: O(S), S is the sum of all the strings in the lists
Space: O(M), where M is the biggest string, if its using Trie, then O(S)
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        self.linkCount = 0

    def addChild(self, char):
        if char not in self.children:
            self.children[char] = TrieNode()
            self.linkCount += 1


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.addChild(char)
            node = node.children[char]
        node.isEnd = True

    def searchLongestPrefix(self, word):
        node = self.root
        chars = []
        for char in word:
            if char in node.children and node.linkCount == 1 and not node.isEnd:
                chars.append(char)
                node = node.children[char]
            else:
                break
        return "".join(chars)


class Solution:
    def longestCommonPrefix(self, q, strs):
        if not strs:
            return ""
            
        if len(strs) == 1:
            return strs[0]

        trie = Trie()

        for s in strs[1:]:
            trie.insert(s)

        return trie.searchLongestPrefix(q)

    def longestCommonPrefix1(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        prefix = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0:
                prefix = prefix[0 : len(prefix) - 1]
                if prefix == "":
                    return ""
        return prefix