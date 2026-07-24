class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        val = sum(nums) // k
        res = [0] * k


        if sum(nums) / k != val:
            return False
        
        nums.sort(reverse=True)

        def backtrack(i):
            if i == len(nums):
                return True 
            seen = set([])

            for j in range(k):
                if res[j] in seen:
                    continue
                seen.add(res[j])

                if res[j] + nums[i] <= val:
                    res[j] += nums[i]
                    if backtrack(i+1):
                        return True 
                    res[j] -= nums[i]
                if res[j] == 0:
                    break
            return False
        return backtrack(0)
                    