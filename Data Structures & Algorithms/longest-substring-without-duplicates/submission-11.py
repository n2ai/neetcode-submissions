class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        hashSet = set()
        maxLength = 0
        while r < len(s):
            if s[r] in hashSet:
                while s[l] != s[r]:
                    hashSet.remove(s[l])
                    l += 1
                l += 1
                
            hashSet.add(s[r])
            maxLength = max(maxLength, (r - l) + 1)
            r += 1
        return maxLength
