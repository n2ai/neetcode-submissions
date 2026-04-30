class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        for right in range(len(nums)):
            if val != nums[right]:
                nums[left] = nums[right]
                left += 1
        
        return left