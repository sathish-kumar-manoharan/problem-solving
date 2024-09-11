"""
https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/submissions/

Time complexity : O(n), where n is the length of the input string.
Space complexity : O(n), where n is the length of the input string.

"""
class Solution:
    
    def minRemoveToMakeValid(self, s: str) -> str:
        if s is None or len(s) == 0:
            return s

        sb = []
        stack = []
        invalid_indexes = set()

        for index, letter in enumerate(s):
            if letter == '(':
                stack.append(index)
            elif letter == ')':
                if stack:
                    stack.pop()
                else:
                    invalid_indexes.add(index)

        while stack:
            invalid_indexes.add(stack.pop())

        for index, letter in enumerate(s):
            if index not in invalid_indexes:
                sb.append(letter)

        return ''.join(sb)
    
    def minRemoveToMakeValid1(self, s: str) -> str:
        
        def remove_invalid_closing(string, open_symbol, close_symbol):
            sb = []
            balance = 0
            
            for char in string:
                if char == open_symbol:
                    balance += 1
                if char == close_symbol:
                    if balance == 0:
                        continue
                    balance -= 1
                    
                sb.append(char)
                
            return "".join(sb)
        
        s = remove_invalid_closing(s, "(", ")")
        s = remove_invalid_closing(s[::-1], ")", "(")
        
        return s[::-1]