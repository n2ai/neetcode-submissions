class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxCount = 0
        hashMap = {}
        l = 0
        result = 0
        for r in range(len(s)):
            window = (r - l) + 1
            hashMap[s[r]] = hashMap.get(s[r], 0) + 1
            val = hashMap[s[r]]
            maxCount = max(maxCount, val)

            if (window - maxCount) > k: 
                hashMap[s[l]] -= 1
                l += 1
            else:
                result = max(result, window)
        
        return result
