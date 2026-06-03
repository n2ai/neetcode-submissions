class Solution:
    def distance(self,x1, y1, x2, y2):
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            distance = -self.distance(0,0,x,y)
            heapq.heappush(heap, (distance,[x,y]))

            if len(heap) > k:
                heapq.heappop(heap)
        
        return [point for _, point in heap]


        
    