"""
https://leetcode.com/problems/valid-word-abbreviation
Time: O(n)
Space: O(1)
"""
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        index = 0
        count = 0

        while index < len(abbr):
            if abbr[index] == '0' or count >= len(word):
                return False
            
            number = ''

            while index < len(abbr) and abbr[index].isdigit():
                number += abbr[index]
                index += 1

            if number:
                count += int(number)
            else:
                if abbr[index] != word[count]:
                    return False

                count += 1
                index += 1

        
        return count == len(word)