from collections import deque
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [i for i in range(n)]
        
        g = [[] for _ in range(n)]
                
        for x,y in edges:
            g[y].append(x)
            g[x].append(y)
        
        q = deque()
        
        for i in range(n):
            if len(g[i]) == 1:
                q.append(i)
        
        r = n
        while r > 2:
            r -= len(q)
            newQ = deque()
            
            while q:
                y = q.popleft()
                x = g[y].pop()
                
                g[x].remove(y)
                if len(g[x]) == 1:
                    newQ.append(x)
                
            q = newQ
        
        return q
            