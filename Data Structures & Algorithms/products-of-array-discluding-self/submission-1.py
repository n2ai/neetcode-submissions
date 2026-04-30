class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1 for _ in nums]
        postfix = [1 for _ in nums]
        for i in range(1, len(nums)):
            prefix[i] = nums[i-1] * prefix[i-1]
        for j in range(len(nums)-2, -1, -1):
            postfix[j] = nums[j+1] * postfix[j+1]
        
        for i in range(0, len(nums)):
            prefix[i] = prefix[i] * postfix[i]
        
        return prefix
        

        # res = [1 for _ in nums]
        # for i in range(1,len(nums)):
        #     res[i] = res[i-1] * nums[i-1]
        # postfix = 1
        # for i in range(len(nums)-1, -1 ,-1):
        #     res[i] *= postfix
        #     postfix *= nums[i]
        # return res