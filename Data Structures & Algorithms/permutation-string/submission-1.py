class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1HashMap = {}
        s2HashMap = {}
        
        # Populate s1HashMap with characters and their counts
        for i in s1:
            if i in s1HashMap:
                s1HashMap[i] += 1
            else:
                s1HashMap[i] = 1

        # Initialize the sliding window
        l = 0
        for r in range(len(s2)):
            if s2[r] in s2HashMap:
                s2HashMap[s2[r]] += 1
            else:
                s2HashMap[s2[r]] = 1
            
            if r - l + 1 > len(s1):
                if s2HashMap[s2[l]] == 1:
                    del s2HashMap[s2[l]]
                else:
                    s2HashMap[s2[l]] -= 1
                l += 1
            
            if s1HashMap == s2HashMap:
                return True
        return False
            
