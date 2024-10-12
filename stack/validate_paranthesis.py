"""
https://leetcode.com/problems/valid-parentheses
Time: O(N)
Space: O(N)
"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        lookup = {")": "(", "}" : "{", "]": "["}
        
        for char in s:
            if char in lookup:
                top_element = stack.pop() if stack else "#"
                
                if lookup[char] != top_element:
                    return False
            else:
                stack.append(char)
                    
            
        return not stack
        