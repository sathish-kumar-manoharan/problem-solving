# T: O(N*M*K), where N is the length of s , M is the length of dictionary and K is the Length of words in dictionary
# S: O(N) 
from typing import List

def wordBreak(s: str, wordDict: List[str]) -> bool:
    dp = [False] * len(s)
    
    for index in range(len(s)):
        for word in wordDict:
            if index < len(word) -1:
                continue
                
            if index == len(word) - 1 or dp[index - len(word)]:
                if s[index - len(word) + 1 : index + 1] == word:
                    dp[index] = True
                    break
                
    print(dp)
    return dp[-1]

    # T: O(N^3 + M*K), where N is the length of s , M is the length of dictionary and K is the Length of words in dictionary
    # S: O(N + M*K) 
    def wordBreak1(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        seen = set()
        
        queue = deque([0])
        
        while queue:
            start = queue.popleft()
            
            if start == len(s):
                return True
            
            for index in range(start + 1, len(s) + 1):
                if index not in seen and s[start : index] in words:
                    queue.append(index)
                    seen.add(index)
                
        return False

wordBreak("leetcode", ["leet", "code"])
