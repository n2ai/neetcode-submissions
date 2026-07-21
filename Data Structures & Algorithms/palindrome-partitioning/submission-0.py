class Solution:
    def checkPalindrome(self,s):
            return s == s[::-1]
    def partition(self, s: str) -> List[List[str]]:

        res = []
        def dfs(i,path):
            if i >= len(s):
                res.append(path.copy())
                return 
            
            for j in range(i, len(s)):
                sub = s[i:j + 1]
                if self.checkPalindrome(sub):
                    path.append(sub)
                    dfs(j + 1,path)
                    path.pop()
        
        dfs(0,[])
        return res
