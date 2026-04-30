class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaMap = {}
        res = []
        for i in strs:
            sortedString = "".join(sorted(i))
            if sortedString in anaMap.keys():
                anaMap[sortedString].append(i)
            else:
                
                 anaMap[sortedString] = [i]
        
        for i in anaMap.values():
            res.append(i)
        
        return res

        
