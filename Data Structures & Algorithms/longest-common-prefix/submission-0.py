class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        curPre = strs[0]
        
        for val in strs[1:]:
            if len(val) < len(curPre):
                curPre = curPre[:len(val)]
            else:
                val = val[:len(curPre)]
            
            for i in range(len(val), -1, -1):
                if val[:i] == curPre[:i]:
                    curPre = curPre[:i]
                    break
        return curPre