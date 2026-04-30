class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashMap = {}
        for i in range(len(nums)):
            val = nums[i]
            if val in hashMap:
                return True
            hashMap[val] = 1
        return False