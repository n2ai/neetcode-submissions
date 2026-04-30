class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        res = set(sorted(nums, key=lambda x: (x < 0, x)))

        for i in range(1, 100000):
            if i not in res:
                return i
        