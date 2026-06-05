class Solution:
    def char_to_index(self,char):
        return ord(char.lower()) - ord('A')
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cycle = 0
        queue = deque([])
        counts = {}
        for task in tasks:
            if task in counts:
                counts[task] += 1
            else:
                counts[task] = 1
        
        heap = [-cnt for cnt in counts.values()]
        heapq.heapify(heap)

        while heap or queue:
            cycle += 1

            if not heap:
                cycle = queue[0][1]
            else:
                cnt = 1 + heapq.heappop(heap)
                if cnt:
                    queue.append([cnt, cycle + n])
            
            if queue and queue[0][1] == cycle:
                heapq.heappush(heap, queue.popleft()[0])
        return cycle




                        

        


        