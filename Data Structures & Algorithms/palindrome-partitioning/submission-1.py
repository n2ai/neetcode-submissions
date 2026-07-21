class Solution:
    def checkPalindrome(self,s):
            return s == s[::-1]
    def partition(self, s: str) -> List[List[str]]:

        res = []

        def dfs(start, path):
            if start == len(s):
                res.append(path.copy())
                return 
            
            for end in range(start, len(s)):
                sub = s[start:end+1]
                if self.checkPalindrome(sub):
                    path.append(sub)
                    dfs(end+1,path)
                    path.pop()

        dfs(0,[])
        return res
            