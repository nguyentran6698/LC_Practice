from collections import Counter, deque
import heapq
from typing import List
def solution(tasks:List[int] , n :int)->int:
    d = Counter(tasks)
    count = [-cnt for cnt in d.values()]

    heapq.heapify(count)

    q = deque()

    time = 0
    while count or q:
        time += 1
        if heapq:
            task = 1 + heapq.heappop(count)
            # task is not 0
            if task:
                q.append([task,time+n])
        
        if q and q[0][1] == time:
            heapq.heappush(count,q.popleft()[0])
    
    return time
tasks = ["A","A","A","B","B","B"]
n = 2
print(solution(tasks,n))