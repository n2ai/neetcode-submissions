class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        COLS = len(grid[0])
        ROWS = len(grid)
        visited = set()
        numOfIsland = 0

        if not grid or not grid[0]:
            return 0

        def dfs(r, c):
            if (r not in range(ROWS) or c not in range(COLS)  or (r, c) in visited or grid[r][c] == "0"):
                return
            visited.add((r, c))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                dfs(r + dr, c + dc)
            


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    numOfIsland += 1
                    dfs(r, c)
        return numOfIsland