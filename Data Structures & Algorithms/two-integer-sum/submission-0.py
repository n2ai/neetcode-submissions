class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        
        for index, value in enumerate(nums):
            needVal = target - value
            if value not in hashMap:
                hashMap[value] = index

            if needVal in hashMap and hashMap[needVal] != index:
                return [hashMap[needVal], index]
        
    