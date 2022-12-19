import collections
from typing import List


class UnionFind:
    def __init__(self,parent):
        self.parent = parent
    def find(self,v):
        if v == self.parent[v]:
            return v
        return self.find(self.parent[v])
    
    def union_set(self,a1,a2):
        s1,s2 = self.find(a1),self.find(a2)
        if s1 != s2:
            self.parent[s2] = s1

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        g = [[] for _ in range(n)]
        for x,y in edges:
            g[y].append(x)
            g[x].append(y)
        parent = [num for num in range(n)]
        uf = UnionFind(parent)
        for a,b in edges:
            uf.union_set(a,b)
        return uf.find(source) == uf.find(destination)

    # BFS
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = [[] for _ in range(n)]
        for x,y in edges:
            graph[y].append(x)
            graph[x].append(y)
        
        # BFS
        seen = [False] * n
        seen[source] = True
        queue = collections.deque([source])

        while queue:
            curr_node = queue.popleft()
            if curr_node == destination:
                return True
            
            for next_node in graph[curr_node]:
                if not seen[next_node]:
                    seen[next_node] = True
                    queue.append(next_node)
        return False
          
    # DFS Iterative
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # Store all edges according to nodes in 'graph'.
        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        # Start from source node, add it to stack.
        seen = [False] * n
        seen[source] = True
        stack = [source]
        
        while stack:
            curr_node = stack.pop()
            # Add all unvisited neighbors of the current node to stack 
            # and mark them as visited.
            for next_node in graph[curr_node]:
                if next_node == destination:
                    return True
                if not seen[next_node]:
                    seen[next_node] = True
                    stack.append(next_node)
    
        return seen[destination]
    
    # DFS 
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            
        seen = [False] * n
        
        def dfs(curr_node):
            if curr_node == destination:
                return True
            if not seen[curr_node]:
                seen[curr_node] = True
                for next_node in graph[curr_node]:
                    if dfs(next_node):
                        return True
            return False
            
        return dfs(source)