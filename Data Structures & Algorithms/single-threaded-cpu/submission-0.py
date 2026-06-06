class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        #sort by enqueue time
        res = []
        time = 0
        indexed_tasks = []
        for i, (enQ, procQ) in enumerate(tasks):
            indexed_tasks.append([enQ,procQ,i])
        
        indexed_tasks.sort()
        i = 0
        minHeap = []
        heapq.heapify(minHeap)
        while i < len(indexed_tasks) or minHeap:
            while i < len(indexed_tasks) and indexed_tasks[i][0] <= time:
                heapq.heappush(minHeap,(indexed_tasks[i][1], indexed_tasks[i][2]))
                i += 1
            if minHeap:
                task = heapq.heappop(minHeap)
                res.append(task[1])
                time += task[0]
            
            if not minHeap and i < len(indexed_tasks):
                time = max(time, indexed_tasks[i][0])
        return res
                
                    