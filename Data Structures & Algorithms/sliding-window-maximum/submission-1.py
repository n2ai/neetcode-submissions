class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        hashSet = {}
        res = []
        l = 0

        for r in range(len(nums)):
            hashSet[nums[r]] = hashSet.get(nums[r], 0) + 1

            while (r - l) + 1 > k:
                delValue = nums[l]
                hashSet[delValue] -= 1       
                if hashSet[delValue] == 0:
                    del hashSet[delValue]     
                l += 1                       

            if (r - l) + 1 == k:
                curMax = max(hashSet) 
                res.append(curMax)

        return res