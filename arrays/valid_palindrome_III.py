"""
https://leetcode.com/problems/valid-palindrome-iii

two pointer 
Time: O(N^2)
space: O(N^2)

"""
from functools import cache

class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        @cache
        def is_palindrome(word, start, end, count):
            while start < end:
                if word[start] != word[end]:
                    if count == 0:
                        return False
                    
                    return is_palindrome(word, start +1, end, count -1) or is_palindrome(word, start, end-1, count-1)
                
                start += 1
                end -= 1
            
            return True
        
        return is_palindrome(s, 0, len(s)-1, k)