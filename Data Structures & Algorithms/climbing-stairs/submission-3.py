class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * n
        def dfs(cur):
            if cur == 0:
                return 1
            if cur < 0:
                return 0
            if cache[cur-1] != -1:
                return cache[cur-1]
            
            cache[cur-1] = dfs(cur - 1) +  dfs(cur - 2)
            return cache[cur-1]
        
        return dfs(n)