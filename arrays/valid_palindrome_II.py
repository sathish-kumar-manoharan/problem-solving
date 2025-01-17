"""
https://leetcode.com/problems/valid-palindrome-ii/description/

two pointer 
Time: O(N)
space: O(1)

"""
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(s, start, end):
            while start < end:
                if s[start] != s[end]:
                    return False
                
                start +=1
                end -= 1

            return True
        
        left, right = 0, len(s)-1

        while left < right:
            if s[left] != s[right]:
                return is_palindrome(s, left, right-1) or is_palindrome(s, left+1, right)
            left += 1
            right -= 1

        return True