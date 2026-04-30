class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        countMap = {}
        res = set([])
        n = len(nums)
        for i in nums:
            if i not in countMap:
                countMap[i] = 1
                if countMap[i] > (n // 3):
                    res.add(i)
                continue
            else:
                countMap[i] += 1
                if countMap[i] > (n // 3):
                    res.add(i)
        return list(res)


        