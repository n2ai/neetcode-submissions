class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict = {}

        if len(s) != len(t):
            return False
        for val in s:
            if val not in sDict:
                sDict[val] = 1
            else:
                sDict[val] += 1

        for val in t:
            if val in sDict:
                sDict[val] -= 1
                if sDict[val] == 0:
                    del sDict[val]
            else:
                return False
        
        if sDict == {}:
            return True
        return False
