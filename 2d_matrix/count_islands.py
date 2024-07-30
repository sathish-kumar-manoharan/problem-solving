# https://leetcode.com/problems/number-of-islands/

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        number_of_islands = 0
        
        if not grid:
            return number_of_islands
        
        rows = len(grid)
        cols = len(grid[0])
        
        seen = [[False]*cols for _ in range(rows)]
               
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and not seen[row][col]:
                    
                    number_of_islands += 1
                    
                    neighbors = [(row, col)]
                    
                    while neighbors:
                        a_row, a_col = neighbors.pop()
                        
                        if a_row-1 >= 0 and grid[a_row-1][a_col] == "1":
                            neighbors.append((a_row-1, a_col))
                            seen[a_row-1][a_col] = True
                            
                        if a_row+1 < rows and grid[a_row+1][a_col] == "1":
                            neighbors.append((a_row+1, a_col))
                            seen[a_row+1][a_col] = True
                            
                        if col-1 >= 0 and grid[a_row][a_col-1] == "1":
                            neighbors.append((a_row, a_col-1))
                            seen[a_row][a_col-1] = True
                            
                        if col+1 < cols and grid[a_row][a_col+1] == "1":
                            neighbors.append((a_row, a_col+1))
                            seen[a_row][a_col+1] = True
                        
                    
        return number_of_islands
    
    def numIslands(self, grid) -> int:
        if not grid:
            return 0
        
        count = 0
        
        visited = [[False]*len(grid[0])]*len(grid)

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                print("The row is ", row, " and the col is ", col)
                if grid[row][col] == "1" and not visited[row][col]:
                    self.dfs(self, grid, row, col, visited)
                    count += 1
                    
        return count
    
    def dfs(self, grid, row, col, visited):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[row]):
            return
        
        if grid[row][col] != "1" or visited[row][col]:
            return
        
        #grid[row][col] = "0"
        visited[row][col] = True
        
        self.dfs(self, grid, row-1, col, visited)
        self.dfs(self, grid, row+1, col, visited)
        self.dfs(self, grid, row, col-1, visited)
        self.dfs(self, grid, row, col+1, visited)

    
solution = Solution

count = solution.numIslands(solution, [["1","0","1","1","0","1","1"]])

print("The number of islands are ", count)