class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        left = 1
        right = piles[-1]
        minK = right
        while left <= right:
            totalHour = 0
            middle = (left + right)//2
            k = middle
            for p in piles:
                totalHour += math.ceil(p / k)

            if totalHour <= h:
                minK = min(minK, k)
                right = middle - 1
            else:
                left = middle + 1

        return minK