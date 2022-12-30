import heapq
from typing import List
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        sorted_tasks = [[task[0],task[1],idx] for idx,task in enumerate(tasks)]
        sorted_tasks.sort()
        curr_time = 0
        taskIdx = 0
        times = []
        res = []
        while taskIdx < len(tasks) or times:
            # need to add task to the queue
            if not times and curr_time < sorted_tasks[taskIdx][0]:
                curr_time = sorted_tasks[taskIdx][0]

            while taskIdx < len(tasks) and curr_time >= sorted_tasks[taskIdx][0]:
                _,timeProces,idx = sorted_tasks[taskIdx]
                heapq.heappush(times,(timeProces,idx))
                taskIdx += 1
            
            processTime,idx = heapq.heappop(times)
            res.append(idx)
            curr_time += processTime
        
        return res
