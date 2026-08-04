class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        visit = set()
        preMap = {i:[] for i in range(numCourses)}
        for val,key in prerequisites:
            preMap[val].append(key)
        
        def dfs(curVal):
            if curVal in visit:
                return False
            
            if preMap[curVal] == []:
                return True
            
            visit.add(curVal)
            for val in preMap[curVal]:
                if not dfs(val):
                    return False 
            visit.remove(curVal)
            preMap[curVal] = []
            return True 

        for r in range(numCourses):
            if not dfs(r):
                return False 
        return True