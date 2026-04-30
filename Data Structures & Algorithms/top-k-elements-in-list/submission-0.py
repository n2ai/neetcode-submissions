from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = defaultdict(int)

        buckets = [ [] for _ in range(len(nums) + 1)]

        for num in nums:
            freqMap[num] += 1
        
        for num, freq in freqMap.items():
            buckets[freq].append(num)

        result = []

        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
        return result