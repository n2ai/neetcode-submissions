class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phoneMap = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno",
                    "7":"pqrs", "8":"tuv", "9":"wxyz"}
        res = []
        if not digits:
            return res
        def dfs(i, path):
            if len(path) == len(digits):
                res.append(''.join(path))
                return 
            curString = phoneMap[digits[(i)]]
            for j in range(len(curString)):
                path.append(curString[j])
                dfs(i+1,path)
                path.pop()
        
        dfs(0,[])
        return res