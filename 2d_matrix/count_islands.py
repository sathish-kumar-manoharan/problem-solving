class Solution:
    def numIslands(self, grid) -> int:
        if not grid:
            return 0
        
        count = 0
        
        visited = [[False]*len(grid[0])]*len(grid)

        print("The number of rows are ", len(visited))
        print("The number of cols are ", len(visited[0]))
        
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