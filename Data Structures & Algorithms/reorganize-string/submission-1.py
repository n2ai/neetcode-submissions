class Solution:
    def reorganizeString(self, s: str) -> str:
        res = ""
        cannot = False
        stringArr = [char for char in s]
        countMap = Counter(stringArr)

        length = len(s)

        for k,v in countMap.items():
            ceil = math.ceil(length/2)
            if v > ceil:
                cannot = True
                break
        
        queue = deque([])
        minHeap = [(-v,k) for (k,v) in countMap.items()]
        heapq.heapify(minHeap)
        prev = None
        while minHeap:
            count, val = heapq.heappop(minHeap)

            res += val 
            count += 1
            
            if prev:
                heapq.heappush(minHeap,prev)
            
            prev = (count, val) if count < 0 else None
            
        
    

        return "" if cannot or prev else res