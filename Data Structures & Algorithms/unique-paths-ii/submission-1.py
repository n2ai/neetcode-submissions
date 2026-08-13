class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        COLS = len(obstacleGrid[0])
        ROWS = len(obstacleGrid)

        def memoization(r,c,cache):
            if r == ROWS or c == COLS or obstacleGrid[r][c] == 1:
                return 0
            
            if r  == ROWS - 1 and c == COLS - 1:
                return 1

            if cache[r][c] != -1:
                return cache[r][c]
            
            cache[r][c] = (memoization(r+1,c,cache) + memoization(r,c+1,cache))
            return cache[r][c]
        
        return memoization(0,0,[[-1]*COLS for _ in range(ROWS)])