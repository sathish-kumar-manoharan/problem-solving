from typing import List

"""
https://leetcode.com/problems/word-search/
Time : O(M*N * 3 ^L)
Space: O(L)
"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word or not board:
            return False

        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == word[0]:
                    if self.dfs(board, row, col, word, 0):
                        return True
        
        return False
    
    def dfs(self, board, row, col, word, index):
        if len(word) == index:
            return True
        
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
            return False

        if board[row][col] != word[index]:
            return False

        temp = board[row][col]
        board[row][col] = '#'

        found = (self.dfs(board, row-1, col, word, index+1) or 
                self.dfs(board, row+1, col, word, index+1) or
                self.dfs(board, row, col-1, word, index+1) or
                self.dfs(board, row, col+1, word, index+1))

        board[row][col] = temp

        return found