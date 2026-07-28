class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        COLS = len(grid[0])
        ROWS = len(grid)

        def dfs(r, c):
            if (min(r,c) < 0 or r == ROWS or c == COLS 
            or grid[r][c] == 0):
                return 0
            
            grid[r][c] = 0
            return (1 + dfs(r + 1, c) +
                        dfs(r - 1, c) +
                        dfs(r, c + 1) +
                        dfs(r, c - 1))
        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = max(dfs(r,c), area)
        
        return area
            
