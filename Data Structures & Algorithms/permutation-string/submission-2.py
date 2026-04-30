class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        maxLen = len(s1)

        def asciiNum(char):
            return ord(char) - ord('a') + 1

        countS1 = [0] * 26
        countS2 = [0] * 26

        for char in s1:
            num = asciiNum(char)
            countS1[num - 1] += 1
        
        l = 0
        print(countS1)
        for r in range(len(s2)):
            if (r - l) + 1 > maxLen:
                numLeft = asciiNum(s2[l])
                countS2[numLeft - 1] -= 1
                l += 1
            numRight = asciiNum(s2[r])
            countS2[numRight - 1] += 1
        
            if countS1 == countS2:
                return True
        return False
