class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        COLS = len(grid[0])
        ROWS = len(grid)
        queue = deque()
        visit = set()
        visit.add((0,0))
        queue.append((0,0))
        
        if(grid[0][0] == 1):
            return -1

        length = 1
        directions = []
        for dr in [-1, 0 , 1]:
            for dc in [-1, 0 , 1]:
                if dr==0 and dc==0:
                    continue
                directions.append([dr,dc])
        
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if ROWS - 1 == r and c == COLS - 1:
                    return length
                
                for dr, dc in directions:
                    if( min(r+dr, c+dc) < 0 or (r+dr) == ROWS or (c+dc) == COLS or (r+dr,c+dc) in visit or 
                    grid[r+dr][c+dc] == 1 ):
                        continue 
                    visit.add((r+dr,c+dc))
                    queue.append((r+dr,c+dc))

            length += 1
        return -1