class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        minValue = float("inf")

        while l <= r:
            m = (l+r)//2
            minValue = min(nums[m],minValue)
            
            if minValue > nums[r]:
                l = m + 1
            else:
                r = m -1
            
        return minValue