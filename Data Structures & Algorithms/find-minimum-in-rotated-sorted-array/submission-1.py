class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        minValue = float("inf")
        while left<=right:
            mid = (left+right)//2
            minValue = min(nums[mid], minValue)
            if minValue > nums[right]:
                left = mid + 1
            else:
                right = mid - 1

        return minValue 
                