class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(cur, open_n, close_n):
            # if open_n > n and count < leftcount:
            #     return 

            if open_n == n == close_n:
                string = "".join(cur)
                res.append(string)
                return 
            
            if(open_n < n):
                cur.append('(')
                dfs(cur, open_n + 1, close_n)
                cur.pop()
            
            if(close_n < open_n):
                cur.append(')')
                dfs(cur, open_n, close_n+1)
                cur.pop()

        dfs([],0,0)
        return res
        