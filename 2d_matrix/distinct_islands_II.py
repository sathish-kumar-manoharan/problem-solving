from typing import List

"""
https://leetcode.com/problems/number-of-distinct-islands-ii/submissions/

Combining this with the outer loop that iterates through the grid, 
the overall time complexity of the numDistinctIslands2 function becomes O(mn(mn + 8log(8))), 
which simplifies to O(m^2n^2 + mn8log(8)).

T: O(MN(MN + 8log(8))) -> O(M^2N^2 + MN8log(8))
S: O(M*N)

"""
class Solution:
    def numDistinctIslands2(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0]) if grid else 0
        
        def dfs(i,j):
            if 0 <= i < rows and 0 <= j < cols and grid[i][j] == 1:
                grid[i][j]=-1
                
                path.append([i,j])
                
                dfs(i,j+1)
                dfs(i+1,j)
                dfs(i,j-1)
                dfs(i-1,j)
                
        def normalize(path):
            rotations = [[] for _ in range(8)]
            
            # rotating in 8 different angles
            for x,y in path:
                rotations[0].append([x,y])       # Original
                rotations[1].append([x,-y])      # Horizontal flip
                rotations[2].append([-x,y])      # Vertical flip
                rotations[3].append([-x,-y])     # Both flips
                rotations[4].append([y,x])       # 90 degrees rotation
                rotations[5].append([y,-x])      # 90 degrees rotation + horizontal flip
                rotations[6].append([-y,x])      # 90 degrees rotation + vertical flip
                rotations[7].append([-y,-x])     # 90 degrees rotation + both flips
                
            for rotation in rotations:
                rotation.sort()
                
                # top left co ordinate
                x0, y0 = rotation[0]
                
                # correcting it to the origin by taking out the top left co ordinate
                for p in rotation:
                    p[0] -= x0
                    p[1] -= y0
                    
            rotations.sort()
            
            return tuple(c for r in rotations[0] for c in r)
        
        distinct_islands=set()
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    path=[]
                    
                    dfs(row,col)

                    distinct_islands.add(normalize(path))

        return len(distinct_islands)