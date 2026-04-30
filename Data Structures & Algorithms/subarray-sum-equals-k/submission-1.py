class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefixMap = {0 : 1}

        prefix = 0
        for num in nums:
            prefix += num
            if prefix - k in prefixMap:
                count += prefixMap[prefix - k]
            
            prefixMap[prefix] = prefixMap.get(prefix, 0) + 1
        
        return count
                
