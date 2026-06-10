class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ''
        prev = deque([]) 
        maxHeap = []
        for count, char in [(-a, 'a'), (-b, 'b'), (-c, 'c')]:
            if count < 0:
                heapq.heappush(maxHeap, (count, char))
        heapq.heapify(maxHeap)
        cannot = False
        while maxHeap:
            heap = heapq.heappop(maxHeap)
            count, val = heap[0], heap[1]
            #condition to pop prev

            if len(res) > 1 and res[-1] == res[-2] == val:  
                if len(maxHeap) == 0:
                    cannot = True
                    break                  
                heap2 = heapq.heappop(maxHeap)
                count2, val2 = heap2[0], heap2[1]
                res += val2
                count2 += 1
                if count2 < 0:
                    heapq.heappush(maxHeap, (count2, val2))
            
            else:
                res += val
                count += 1
            if count < 0:
                heapq.heappush(maxHeap, (count, val))
            
        return res if cannot == False else res
                

