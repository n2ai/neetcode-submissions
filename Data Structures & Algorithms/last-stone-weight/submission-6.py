class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
          negStones = [-item for item in stones]
          if len(stones) == 1:
            return stones[0]
          
          while len(negStones) > 1:
            heapq.heapify(negStones)
            first = heapq.heappop(negStones)
            second = heapq.heappop(negStones)

            left = abs(abs(first) - abs(second))
            print(left)
            print(negStones)
            if left != 0 :
                heapq.heappush(negStones, -left)

          return 0 if len(negStones) == 0 else -negStones[0]