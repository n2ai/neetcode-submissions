class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        COLS = len(grid[0])
        ROWS = len(grid)
        queue = deque([])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r,c))
                if grid[r][c] == 1:
                    fresh += 1
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
       
        time = 0
        while queue:
            if(fresh == 0):
                return time

            for i in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr = r + dr 
                    nc = c + dc 
                    if(min(nr,nc) < 0 or COLS == nc or ROWS == nr or 
                        grid[nr][nc] == 2 or grid[nr][nc] == 0):
                        continue
                    queue.append((nr,nc))
                    fresh-=1
                    grid[nr][nc] = 2
            time += 1
        
        return -1 if fresh != 0 else 0

        

        