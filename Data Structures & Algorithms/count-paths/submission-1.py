class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        def memoization(r,c,rows,cols,cache):
            if r == rows or c == cols:
                return 0
            
            if cache[r][c] > 0:
                return cache[r][c]

            if r == rows - 1 or c == cols - 1:
                return 1 
            
            cache[r][c] = memoization(r + 1,c,rows,cols, cache) + memoization(r,c+1,rows,cols,cache)
            return cache[r][c]
        
        return memoization(0,0,m,n,[[0]*n for _ in range(m) ] )

            