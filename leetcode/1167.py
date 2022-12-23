import heapq
from typing import List
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        # min heap
        heapq.heapify(sticks)
        minCost = 0

        while len(sticks) > 1:
            s1 = heapq.heappop(sticks)
            s2 = heapq.heappop(sticks)
            
            minCost += (s1 + s2)

            heapq.heappush(sticks,s1+s2)
        return minCost
