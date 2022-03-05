# Minimum Path Sum (leetcode)

# Top-down Iterative
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        for i in range(m - 2, -1, -1):
            grid[i][n - 1] += grid[i + 1][n - 1]
            
        prev_row = [float('inf')]*n
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 2, -1, -1):
                grid[i][j] += min(grid[i][j + 1], prev_row[j])
                prev_row[j] = grid[i][j]
        
        return grid[0][0]