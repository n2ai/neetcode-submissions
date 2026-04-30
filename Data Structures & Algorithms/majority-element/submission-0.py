class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        count = 0
        
        for val in nums:
            if count == 0:
                candidate = val

            if val == candidate:
                count+=1
            else:
                count -= 1
        return candidate
