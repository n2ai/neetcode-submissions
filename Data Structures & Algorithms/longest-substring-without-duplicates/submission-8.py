class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l, r = 0, 0
        maxLength = 0
        while r < len(s):
            print(charSet)
            while s[r] in charSet:
                charSet.remove(s[l])
                l +=1 
            charSet.add(s[r])
            maxLength = max((r-l) +1 ,maxLength)
            r += 1
        return maxLength
            

