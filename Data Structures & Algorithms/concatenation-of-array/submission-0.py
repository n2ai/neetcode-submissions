class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * 2 * n
        for index, value in enumerate(nums):
            ans[index] = ans[index + n] = nums[index]
        return ans