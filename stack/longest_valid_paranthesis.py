"""
https://leetcode.com/problems/longest-valid-parentheses/
"""
class Solution:
    """
    Time: O(N)
    Space: O(1)
    """
    def longestValidParentheses(self, s: str) -> int:

        max_count, left, right = 0, 0, 0

        for index in range(len(s)):
            if s[index] == "(":
                left += 1
            else:
                right += 1
            
            if left == right:
                max_count = max(max_count, 2 * right)
            elif right > left:
                left = right = 0
                
        left = right = 0
        for index in range(len(s)-1, -1, -1):
            if s[index] == "(":
                left += 1
            else:
                right += 1
            
            if left == right:
                max_count = max(max_count, 2 * left)
            elif left > right:
                left = right = 0

        return max_count

    """
    Time: O(N)
    Space: O(N)
    """
    def longestValidParentheses1(self, s: str) -> int:
        stack = [-1]
        max_count = 0

        for index in range(len(s)):
            if s[index] == '(':
                stack.append(index)
            else:
                stack.pop()
                if not stack:
                    stack.append(index)
                else:
                    max_count = max(max_count, index - stack[-1])
        return max_count
