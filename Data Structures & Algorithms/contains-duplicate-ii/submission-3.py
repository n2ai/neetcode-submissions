class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashSet = set()
        l = 0
        for r in range(0,len(nums)):
            if (r - l) > k:
                hashSet.remove(nums[l])
                l += 1
            
            if nums[r] in hashSet:
                return True
            else:
                hashSet.add(nums[r])

        return False
