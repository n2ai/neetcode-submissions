class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        COLS = len(grid[0])
        ROWS = len(grid)
        visited = set()
        area = 0
        def dfs(r, c):
            if (r not in range(ROWS) or c not in range(COLS)
                or (r, c) in visited or grid[r][c] == 0):
                return 0
            
            visited.add((r, c))
            curr_area = 1
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                curr_area += dfs(r + dr, c + dc)
            return curr_area
            
        for r in range(ROWS):
            for c in range(COLS):
                if ((r, c) not in visited and grid[r][c] == 1):
                    area = max(area, dfs(r, c))
        return area