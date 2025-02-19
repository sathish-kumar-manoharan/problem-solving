"""
https://leetcode.com/problems/shortest-word-distance-ii/
"""

from collections import defaultdict
from typing import List


class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.lookup = defaultdict(list)

        for index, word in enumerate(wordsDict):
            self.lookup[word].append(index)

    # Time: O(N)
    # Space: O(n)
    def shortest(self, word1: str, word2: str) -> int:
        l1, l2 = self.lookup[word1], self.lookup[word2]

        p1 , p2 = 0, 0

        min_distance = float('inf')

        while p1 < len(l1) and p2 < len(l2):
            min_distance = min(min_distance, abs(l1[p1] - l2[p2]))

            if l1[p1] < l2[p2]:
                p1 += 1
            else:
                p2 += 1

        return min_distance


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)