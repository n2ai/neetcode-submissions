class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLen = float('inf')
        l = 0
        total = 0
        for r in range(len(nums)):
            valRight = nums[r]
            total += valRight
            print(total)
            while total >= target:
                diff = (r - l) + 1
                minLen = min(minLen, diff)
                total -= nums[l]
                l += 1
            
        if minLen == float('inf'):
            return 0
        else:
            return minLen
