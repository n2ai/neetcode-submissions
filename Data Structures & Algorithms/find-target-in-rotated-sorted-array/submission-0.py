class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(left, right):
            while left <= right:
                mid = (left + right)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return -1
        
        l = 0
        r = len(nums) - 1

        while l < r:
            m = (l + r)//2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        index = -1

        if l != 0:
            index = binarySearch(0, l - 1)
            if index != -1:
                return index

        return binarySearch(l, len(nums) - 1)
